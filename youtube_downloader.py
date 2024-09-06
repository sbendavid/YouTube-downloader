import yt_dlp

DOWNLOAD_DIR = 'c:\\Users\\samue\\OneDrive\\Downloads'

def download_video_yt_dlp(link):
    try:
        ydl_opts = {'outtmpl': f'{DOWNLOAD_DIR}/%(title)s.%(ext)s'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print("Download completed!")
    except Exception as e:
        print(f"An error occurred while downloading the video: {e}")

def download_playlist_yt_dlp(link):
    try:
        ydl_opts = {
            'outtmpl': f'{DOWNLOAD_DIR}/%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s',
            'noplaylist': False  # Ensures that the entire playlist is downloaded
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print("Playlist download completed!")
    except Exception as e:
        print(f"An error occurred while downloading the playlist: {e}")

def main():
    video_type = input("Type 's' for a single video and 'p' for a playlist: ")

    if video_type == "s":
        link = input("Enter the URL of the video to download: ")
        download_video_yt_dlp(link)
    elif video_type == "p":
        link = input("Enter the URL of the playlist to download: ")
        download_playlist_yt_dlp(link)
    else:
        print("Invalid option! Please choose either 's' for single video or 'p' for playlist.")

if __name__ == "__main__":
    main()
