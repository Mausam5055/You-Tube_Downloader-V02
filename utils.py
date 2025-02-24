import yt_dlp
import os
from yt_dlp.utils import DownloadError

def ensure_directory(path):
    """Ensure the directory exists, if not, create it."""
    if not os.path.exists(path):
        os.makedirs(path)

def download_video(url, path, progress_callback=None):
    """
    Downloads a YouTube video with both video and audio properly merged.
    """
    try:
        ensure_directory(path)

        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',  # Forces MP4 video and M4A audio
            'merge_output_format': 'mp4',  # Ensures merging into a single file
            'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),  # Save in Downloads folder
            'postprocessors': [{
                'key': 'FFmpegMerger',  # Forces proper merging of video and audio
            }],
            'progress_hooks': [progress_callback] if progress_callback else [],
            'noplaylist': True,  # Only downloads a single video
            'quiet': False,  # Show progress output
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            info = ydl.extract_info(url, download=False)

        return os.path.join(path, ydl.prepare_filename(info))

    except DownloadError as e:
        raise RuntimeError(f"Download Error: {e}")
    except Exception as e:
        raise RuntimeError(f"Unexpected Error: {e}")

def convert_to_mp3(url, path, progress_callback=None):
    """
    Downloads a YouTube video and converts it to MP3.
    """
    try:
        ensure_directory(path)

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),  # Save in Downloads folder
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'progress_hooks': [progress_callback] if progress_callback else [],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            info = ydl.extract_info(url, download=False)

        return os.path.join(path, ydl.prepare_filename(info).replace('.webm', '.mp3').replace('.m4a', '.mp3'))

    except DownloadError as e:
        raise RuntimeError(f"MP3 Conversion Error: {e}")
    except Exception as e:
        raise RuntimeError(f"Unexpected Error: {e}")
