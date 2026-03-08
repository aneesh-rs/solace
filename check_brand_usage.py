"""
check_brand_usage.py - Check brand name usage on the web via Bing Web Search API

USAGE:
  - Place your Bing API key in a .env file as BING_API_KEY=YOUR_KEY
  - OR when prompted, paste your key (optionally save to .env)
  - Run: python check_brand_usage.py
  - Follow on-screen instructions to enter a brand name

REQUIREMENTS:
  - requests
  - python-dotenv (for .env support)

"""

import os
import sys
import requests

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    print(
        "[INFO] The 'python-dotenv' package is not installed. For better security and convenience, please install it by running: pip install python-dotenv\nYou can also continue without it, but .env support will not work."
    )


def get_api_key():
    api_key = os.environ.get("BING_API_KEY")
    if not api_key or api_key == "YOUR_BING_API_KEY":
        print("\nYou must provide a Bing Web Search API key.")
        api_key = input("Paste your Bing API key (input stays hidden): ").strip()
        if api_key:
            save = input("Save this key to a .env file for future use? [y/n]: ").lower()
            if save == "y":
                try:
                    with open(".env", "a") as f:
                        f.write(f"\nBING_API_KEY={api_key}\n")
                    print("Saved API key to .env")
                except Exception as e:
                    print(f"Could not save to .env: {e}")
        else:
            print("No API key provided. Exiting.")
            sys.exit(1)
    return api_key


def check_brand_name_usage():
    subscription_key = get_api_key()
    search_url = "https://api.bing.microsoft.com/v7.0/search"

    while True:
        brand_name = input(
            "\nEnter a brand name to check (or type 'exit' to quit): "
        ).strip()
        if not brand_name or brand_name.lower() == "exit":
            print("Goodbye!")
            break
        headers = {"Ocp-Apim-Subscription-Key": subscription_key}
        params = {"q": brand_name, "textFormat": "HTML"}

        print(f"\nSearching the web for '{brand_name}'...")
        try:
            response = requests.get(
                search_url, headers=headers, params=params, timeout=10
            )
            response.raise_for_status()
            web_data = response.json()
        except requests.exceptions.HTTPError as e:
            if response.status_code == 401:
                print(
                    "[ERROR] Authentication failed: Invalid API key. Please check your BING_API_KEY."
                )
            else:
                print(f"[ERROR] HTTP error: {e}")
            continue
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Request/network error: {e}")
            continue
        except Exception as e:
            print(f"[ERROR] Unexpected error: {e}")
            continue

        total_matches = web_data.get("webPages", {}).get("totalEstimatedMatches", 0)
        results = web_data.get("webPages", {}).get("value", [])

        prominent_hits = 0
        for result in results:
            title = result.get("name", "").lower()
            url = result.get("url", "").lower()
            if brand_name.lower() in title or brand_name.lower() in url:
                prominent_hits += 1
        print(f"\n============================")
        print(f"Total search results: {total_matches}")
        print(
            f"Top {len(results)} results contain '{brand_name}' in the title or URL: {prominent_hits}"
        )

        threshold = 1000000  # You can adjust
        if total_matches > threshold or prominent_hits > (len(results) // 2):
            print(f"\n❗ The brand name '{brand_name}' appears to be heavily used.")
        else:
            print(
                f"\n✅ The brand name '{brand_name}' does NOT appear to be heavily used."
            )
        print("============================\n")
        print("(Done using Bing Web Search API)")
        # Optionally allow the user to try again or quit


if __name__ == "__main__":
    print("""
========================
Brand Name Usage Checker
========================
This script checks if a brand name is heavily used by querying Bing Web Search API.
""")
    check_brand_name_usage()
