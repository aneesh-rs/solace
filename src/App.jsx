// Solace Landing Page
import './App.css'

function RoomBubble({ name }) {
  return <span className="room-bubble">{name}</span>;
}

function App() {
  return (
    <main>
      <div className="solace-logo">Solace</div>
      <div className="solace-tagline">Ambient social rooms for quiet connections</div>
      <section className="solace-section">
        <h2 style={{marginTop:0, fontSize:'1.18rem'}}>Why Solace?</h2>
        <p>Lonely online? Most platforms focus on content, not simple presence. Solace lets you join themed rooms and share quiet human presence — like a digital café or study room.</p>
      </section>

      <section className="solace-section">
        <h2 style={{marginTop:0, fontSize:'1.18rem'}}>Example Rooms</h2>
        <div className="room-list">
          <RoomBubble name="☕ Coffee Break" />
          <RoomBubble name="📚 Study Room" />
          <RoomBubble name="💡 Deep Work" />
          <RoomBubble name="🌙 Chill Room" />
        </div>
      </section>

      <section className="solace-section">
        <h2 style={{marginTop:0, fontSize:'1.18rem'}}>How it Works</h2>
        <ul style={{paddingLeft:'1.2em',margin:'0.7em 0 0.3em 0'}}> 
          <li>Browse & join a room instantly</li>
          <li>Sit quietly, react, or optionally speak</li>
          <li>No profiles, no feeds, no pressure</li>
        </ul>
        <span className="react-examples">👋 👍 ☕ ❤️</span>
        <div style={{marginTop:'0.4em',fontSize:'0.96rem',color:'#65747c'}}>Lightweight presence & reactions</div>
      </section>

      <section className="solace-section" style={{fontSize:'0.95em',background:'#f7f7fb'}}> 
        <div><b>MVP:</b> Room list • Join/leave • Presence bubbles • Simple reactions</div>
        <div style={{fontSize:'0.94em',marginTop:'0.4em',color:'#a6a0c0'}}>Designed for remote workers, students, night owls, anyone seeking subtle connection.</div>
      </section>
      <footer style={{margin:'1.2em 0 0 0', fontSize:'0.93em',color:'#888'}}>Solace — Lightweight moments of togetherness online.</footer>
    </main>
  )
}

export default App
