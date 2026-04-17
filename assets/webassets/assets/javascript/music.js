let musicLibrary = [];

// Korrekter Pfad von musicplayer.html (in othertabs/) aus
const MUSIC_JSON_PATH = "../assets/music/music-list.json";

async function loadMusicLibrary() {
  const resultsContainer = document.getElementById("searchResults");
  
  try {
    console.log("Versuche JSON zu laden von:", MUSIC_JSON_PATH);
    
    const response = await fetch(MUSIC_JSON_PATH);
    
    if (!response.ok) {
      throw new Error(`HTTP Fehler: ${response.status}`);
    }

    const data = await response.json();
    musicLibrary = data.music || [];
    
    console.log(`✅ ${musicLibrary.length} Songs erfolgreich geladen!`);
    renderLibrary(musicLibrary);

  } catch (err) {
    console.error("Ladefehler:", err);
    resultsContainer.innerHTML = `
      <p style="color:#ff6666; text-align:center; padding:25px; line-height:1.6;">
        <strong>music-list.json nicht gefunden.</strong><br><br>
        Versuchte Pfad: <code>${MUSIC_JSON_PATH}</code><br><br>
        Bitte überprüfe:<br>
        • Liegt die Datei wirklich in <strong>assets/music/music-list.json</strong>?<br>
        • Öffnest du musicplayer.html mit Live Server?<br>
        • Dateiname ist exakt "music-list.json"
      </p>`;
  }
}

function searchMusic() {
  const query = document.getElementById("searchInput").value.toLowerCase().trim();
  const container = document.getElementById("searchResults");

  if (!query) {
    renderLibrary(musicLibrary);
    return;
  }

  const filtered = musicLibrary.filter(track => 
    track.title.toLowerCase().includes(query) || 
    (track.artist && track.artist.toLowerCase().includes(query))
  );

  renderLibrary(filtered);
}

function renderLibrary(tracks) {
  const container = document.getElementById("searchResults");
  container.innerHTML = "";

  if (tracks.length === 0) {
    container.innerHTML = `<p style="text-align:center; padding:30px; opacity:0.7;">Keine Songs gefunden</p>`;
    return;
  }

  tracks.forEach(track => {
    const div = document.createElement("div");
    div.className = "track-result";
    div.innerHTML = `
      <div style="flex:1;">
        <strong>${track.title}</strong><br>
        <small>${track.artist || 'Unbekannter Artist'}</small>
      </div>
      <button onclick="playLocalTrack('${track.file}')">▶ Play</button>
    `;
    container.appendChild(div);
  });
}

function playLocalTrack(filename) {
  const audio = document.getElementById("audio");
  const fullPath = `../assets/music/${filename}`;

  console.log("Spiele:", fullPath);

  audio.src = fullPath;
  audio.play().catch(err => {
    console.error("Play Fehler:", err);
    alert("Konnte die Datei nicht abspielen.\nPfad: " + fullPath);
  });

  const track = musicLibrary.find(t => t.file === filename);
  if (track) {
    document.getElementById("title").textContent = track.title;
    document.getElementById("artist").textContent = track.artist || '';
  }
}

// Beim Laden der Seite starten
window.addEventListener('load', loadMusicLibrary);