from flask import Flask, render_template, request, jsonify
from utils import download_video, convert_to_mp3
import os
import threading
import uuid
import time
import platform

app = Flask(__name__)

# Function to get the system download folder
def get_download_path():
    system = platform.system()
    
    if system == "Windows":
        return os.path.join(os.environ["USERPROFILE"], "Downloads")  # C:\Users\Username\Downloads
    elif system == "Darwin":  # macOS
        return os.path.join(os.path.expanduser("~"), "Downloads")
    else:  # Linux & Android
        return os.path.join(os.path.expanduser("~"), "Downloads")

DOWNLOAD_FOLDER = get_download_path()  # Set download folder based on OS

# Store progress data for downloads
progress_data = {}

@app.route('/')
def index():
    print("[LOG] Page loaded")  # Debugging
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    url = data.get('url')
    format_type = data.get('format', 'mp4')

    print(f"[LOG] Download request received for URL: {url}, Format: {format_type}")  # Debugging

    if not url:
        return jsonify({'error': 'No URL provided'}), 400

    task_id = str(uuid.uuid4())  # Generate a unique ID for this download
    progress_data[task_id] = {"progress": 0, "status": "starting"}

    # Run the download in a separate thread to avoid blocking the server
    def process_download(task_id, url, format_type):
        try:
            for i in range(1, 11):  # Simulating progress update
                progress_data[task_id] = {"progress": i * 10, "status": "downloading"}
                time.sleep(1)

            if format_type == 'mp3':
                file_path = convert_to_mp3(url, DOWNLOAD_FOLDER)
            else:
                file_path = download_video(url, DOWNLOAD_FOLDER)

            progress_data[task_id] = {"progress": 100, "status": "completed", "file": file_path}
            print(f"[LOG] Download complete: {file_path}")  # ✅ Printed in terminal only

        except Exception as e:
            print(f"[ERROR] {e}")  # ✅ Error printed in terminal only
            progress_data[task_id] = {"progress": 100, "status": "error", "message": str(e)}

    # Start the download process in a new thread
    threading.Thread(target=process_download, args=(task_id, url, format_type)).start()

    return jsonify({'task_id': task_id})

@app.route('/progress/<task_id>', methods=['GET'])
def progress(task_id):
    if task_id in progress_data:
        return jsonify(progress_data[task_id])
    else:
        return jsonify({"error": "Task not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
