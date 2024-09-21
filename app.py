from flask import Flask, render_template, request
import yt_dlp
import os
import platform

app = Flask(__name__)

def get_download_directory():
    """Determine the user's default Downloads directory."""
    home = os.path.expanduser("~")
    if platform.system() == "Windows":
        return os.path.join(home, "Downloads")
    elif platform.system() == "Darwin":  # macOS
        return os.path.join(home, "Downloads")
    else:  # Assume Linux
        return os.path.join(home, "Downloads")

def download_video_yt_dlp(link, resolution):
    download_dir = get_download_directory()
    try:
        format_option = f'bestvideo[height>={resolution}]+bestaudio/best[height>={resolution}]'
        ydl_opts = {
            'outtmpl': f'{download_dir}/%(title)s.%(ext)s',
            'format': format_option,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        return "Download completed!"
    except Exception as e:
        return f"An error occurred while downloading the video: {e}"

def download_playlist_yt_dlp(link, resolution):
    download_dir = get_download_directory()
    try:
        format_option = f'bestvideo[height>={resolution}]+bestaudio/best[height>={resolution}]'
        ydl_opts = {
            'outtmpl': f'{download_dir}/%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s',
            'format': format_option,
            'noplaylist': False,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        return "Playlist download completed!"
    except Exception as e:
        return f"An error occurred while downloading the playlist: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        link = request.form.get('link')
        resolution = request.form.get('resolution')
        download_type = request.form.get('download_type')
        
        if not link or not resolution:
            return "Please enter link and resolution."

        if download_type == 'video':
            message = download_video_yt_dlp(link, resolution)
        elif download_type == 'playlist':
            message = download_playlist_yt_dlp(link, resolution)
        else:
            return "Invalid download type selected."

        return render_template('index.html', message=message)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
