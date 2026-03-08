import requests


def check_brand_name_usage():
    subscription_key = "YOUR_BING_API_KEY"  # Replace with your Bing Web Search API key
    search_url = "https://api.bing.microsoft.com/v7.0/search"

    brand_name = input("Enter a brand name to check: ").strip()
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    params = {"q": brand_name, "textFormat": "HTML"}

    print("Searching the web for '{}'...".format(brand_name))
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    web_data = response.json()

    total_matches = web_data.get("webPages", {}).get("totalEstimatedMatches", 0)
    results = web_data.get("webPages", {}).get("value", [])

    prominent_hits = 0
    for result in results:
        title = result.get("name", "").lower()
        url = result.get("url", "").lower()
        if brand_name.lower() in title or brand_name.lower() in url:
            prominent_hits += 1
    print(f"\nTotal search results: {total_matches}")
    print(
        f"Top {len(results)} results contain '{brand_name}' in the title or URL: {prominent_hits}"
    )

    threshold = 1000000  # You can adjust
    if total_matches > threshold or prominent_hits > (len(results) // 2):
        print(f"\n❗ The brand name '{brand_name}' appears to be heavily used.")
    else:
        print(f"\n✅ The brand name '{brand_name}' does NOT appear to be heavily used.")
    print("\n(Done using Bing Web Search API)")


if __name__ == "__main__":
    check_brand_name_usage()
