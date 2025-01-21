document.getElementById("connectBtn").addEventListener("click", async () => {
    try {
      // Call the backend to connect accounts
      const response = await fetch("http://127.0.0.1:5000/connect"); // Adjust URL if needed
      const data = await response.json();
      
      if (data.success) {
        alert("Accounts connected! Generating playlist...");
        fetchPlaylist(); // Fetch playlist once connected
      } else {
        alert("Failed to connect accounts. Try again.");
      }
    } catch (error) {
      console.error("Error:", error);
      alert("Something went wrong.");
    }
  });
  
  async function fetchPlaylist() {
    try {
      const response = await fetch("http://127.0.0.1:5000/playlist"); // Backend route for fetching playlist
      const data = await response.json();
      
      if (data.success) {
        const playlist = data.playlist;
        const resultsDiv = document.getElementById("results");
        const playlistList = document.getElementById("playlist");
  
        // Clear previous results
        playlistList.innerHTML = "";
  
        // Add each track to the list
        playlist.forEach(track => {
          const li = document.createElement("li");
          li.textContent = `${track.name} by ${track.artist}`;
          playlistList.appendChild(li);
        });
  
        resultsDiv.style.display = "block"; // Show results
      } else {
        alert("Failed to fetch playlist.");
      }
    } catch (error) {
      console.error("Error:", error);
      alert("Something went wrong.");
    }
  }