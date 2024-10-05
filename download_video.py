from pytube import YouTube
from pytube.exceptions import VideoUnavailable
import sys

def progress_function(stream, chunk, bytes_remaining):
    """Callback function to show download progress."""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    
    # Calculate percentage completed
    percentage_of_completion = (bytes_downloaded / total_size) * 100
    
    # Display progress in the same line
    sys.stdout.write(f"\rDownloading... {percentage_of_completion:.2f}% completed")
    sys.stdout.flush()

def download_video(url, save_path="."):
    try:
        yt = YouTube(url, on_progress_callback=progress_function)
        
        # Check if the video is available
        if yt is None:
            raise VideoUnavailable("The video is unavailable.")

        # Filter streams for a video resolution of 720p
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        
        if stream is None:
            print("720p resolution not available for this video.")
            return

        print(f"Starting download: {yt.title} in 720p")
        stream.download(output_path=save_path)
        print(f"Downloaded successfully! Video saved to: {save_path}")
    
    except VideoUnavailable:
        print(f"Video {url} is unavailable.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # https://www.youtube.com/watch?v=3FNYvj2U0HM&list=PLLKT__MCUeixqHJ1TRqrHsEd6_EdEvo47&index=3&t=107s
    # https://www.youtube.com/watch?v=sH4JCwjybGs&list=PLLKT__MCUeixqHJ1TRqrHsEd6_EdEvo47&index=2
    video_url = "https://www.youtube.com/watch?v=sH4JCwjybGs&list=PLLKT__MCUeixqHJ1TRqrHsEd6_EdEvo47&index=2"
    download_path = "c:\\Users\\samue\\OneDrive\\Downloads"
    
    download_video(video_url, download_path)
