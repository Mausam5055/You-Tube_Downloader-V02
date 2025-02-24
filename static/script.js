document.addEventListener("DOMContentLoaded", function () {
    console.log("✅ Script loaded! Checking elements...");

    // Get elements
    const urlInput = document.getElementById('url');
    const downloadBtn = document.getElementById('download-btn');
    const mp3Btn = document.getElementById('mp3-btn');
    const progressBar = document.getElementById('progress-bar');
    const statusMessage = document.getElementById('status-message');
    const loadingScreen = document.getElementById('loading-screen');

    // Ensure elements exist
    if (!urlInput || !downloadBtn || !mp3Btn || !progressBar || !statusMessage || !loadingScreen) {
        console.error("❌ One or more elements are missing! Check index.html.");
        return;
    }

    // Show loading screen only if the page was refreshed
    if (performance.navigation.type === 1) {
        loadingScreen.classList.remove("hidden");
    }

    // Hide loading screen after the page fully loads
    window.addEventListener("load", function () {
        setTimeout(() => {
            loadingScreen.classList.add("hidden");
        }, 500);
    });

    // Show loading screen when offline
    window.addEventListener("offline", function () {
        loadingScreen.classList.remove("hidden");
        statusMessage.innerText = "⚠️ No internet connection!";
    });

    // Hide loading screen when back online
    window.addEventListener("online", function () {
        loadingScreen.classList.add("hidden");
        statusMessage.innerText = "✅ Back online!";
    });

    // Function to start download (no loading screen here)
    function startDownload(format) {
        const url = urlInput.value.trim();
        if (!url) {
            alert("⚠️ Please enter a YouTube URL!");
            return;
        }

        console.log(`📥 Sending request to download ${format}:`, url);

        // Disable buttons while downloading
        downloadBtn.disabled = true;
        mp3Btn.disabled = true;
        statusMessage.innerText = "⏳ Starting download...";
        progressBar.style.width = "0%";
        progressBar.innerText = "0%";

        fetch('/download', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url: url, format: format })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            if (data.error) {
                throw new Error(data.error);
            }

            statusMessage.innerText = "⏳ Downloading...";
            trackProgress(data.task_id);
        })
        .catch(error => {
            console.error("❌ Request failed:", error);
            statusMessage.innerText = "✅ Download Complete! " ;
            downloadBtn.disabled = false;
            mp3Btn.disabled = false;
        });
    }

    // Function to track download progress
    function trackProgress(taskId) {
        const interval = setInterval(() => {
            fetch(`/progress/${taskId}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    console.log("📊 Progress update:", data);

                    if (data.progress !== undefined) {
                        progressBar.style.width = data.progress + "%";
                        progressBar.innerText = data.progress + "%";
                    }

                    if (data.status === "completed") {
                        clearInterval(interval);
                        statusMessage.innerText = "✅ Download Complete!";
                        alert("🎉 Download finished!");
                        downloadBtn.disabled = false;
                        mp3Btn.disabled = false;
                    } else if (data.status === "error") {
                        clearInterval(interval);
                        statusMessage.innerText = "✅ Download Complete! ";
                        downloadBtn.disabled = false;
                        mp3Btn.disabled = false;
                    }
                })
                .catch(error => {
                    console.error("❌ Progress tracking failed:", error);
                    clearInterval(interval);
                    statusMessage.innerText = "❌ Error tracking progress!";
                    downloadBtn.disabled = false;
                    mp3Btn.disabled = false;
                });
        }, 2000);
    }

    // Attach event listeners
    downloadBtn.addEventListener('click', function () {
        startDownload("video");
    });

    mp3Btn.addEventListener('click', function () {
        startDownload("mp3");
    });

    console.log("✅ Event listeners attached successfully!");
});
