# YouTube Video & MP3 Downloader 🎥🎵

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Flask](https://img.shields.io/badge/Framework-Flask-green)](https://flask.palletsprojects.com/)

A simple Flask-based web app to download YouTube videos as MP4 or convert them to MP3.

## Table of Contents
- [Features](#-features)
- [Preview](#-preview)
- [Installation & Setup](#-installation--setup)
- [Troubleshooting](#-troubleshooting)
- [License](#-license)
- [Author](#-author)

## 🚀 Features
- 📥 Download YouTube videos in MP4 format
- 🎧 Convert YouTube videos to MP3 audio
- 📊 Track download progress in real-time
- 📱 Fully responsive UI with modern design

---

## 📌 Preview
![Preview Image](preview.png)  


---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7+
- FFmpeg (for MP3 conversion)
- Stable internet connection

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Virtual Environment Setup
```bash
# Create virtual environment
python -m venv venv

# Activate environment
# Windows:
venv\Scripts\activate
# MacOS/Linux:
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ FFmpeg Installation

#### Windows
- Download from [FFmpeg Official Builds](https://ffmpeg.org/download.html)
- Extract ZIP and add `ffmpeg/bin` to system PATH
- Verify installation:
```cmd
ffmpeg -version
```

#### MacOS (Homebrew)
```bash
brew install ffmpeg
```

#### Linux (Debian/Ubuntu)
```bash
sudo apt update && sudo apt install ffmpeg
```

### 5️⃣ Run Application
```bash
python app.py
# For custom port:
python app.py --port 10000
```
Access the app at: [http://localhost:10000](http://localhost:10000)

---

## 🔧 Troubleshooting

| Issue                   | Solution                                     |
|-------------------------|---------------------------------------------|
| FFmpeg not found       | Verify PATH configuration, restart terminal |
| Dependency errors      | Update pip: `pip install --upgrade pip`    |
| Port already in use    | Use different port: `--port 5000`          |
| Download fails         | Check YouTube URL validity                 |

---

## 🌜 License
Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

---

## 👨‍💻 Author
**Mausam Kar**  
[GitHub](https://github.com/your-username)  
Contributions & suggestions welcome! 🚀

---

## 🚀 What's Next?
- Add playlist support
- Implement quality selection
- Add download history tracking

