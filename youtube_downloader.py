from pytube import YouTube, Playlist
from pytube.exceptions import PytubeError
from http.client import IncompleteRead

# Set the output path for the downloaded file
# Set the part to the download dir or any part
DOWNLOAD_DIR = 'c:\\Users\\samue\\OneDrive\\Downloads'

print("YouTube Downloader!")
print("Welcome to my youtube downloader!")
print(
    "This script allows you to download YouTube videos in a specified resolution range.\n"
    "Make sure you have the pytube library installed by running 'pip install pytube'.\n"
    "Make sure to replace the example links with your own YouTube links.\n"
    "Note: Make sure the download directory is accessible."
)

def single_video(link):
    try:
        max_retries = 3

        # Create a YouTube object
        yt = YouTube(link)

        # Get the highest resolution stream
        yt_stream = yt.streams.get_highest_resolution()

        # Print video details
        print(f"Video Title: {yt.title}")
        print(f"Resolution: {yt_stream.resolution}")

        # Get file size in bytes
        file_size = yt_stream.filesize

        # Convert bytes to megabytes for better readability
        file_size_mb = file_size / (1024 * 1024)
        print(f"File Size: {file_size_mb:.2f} MB")

        # Download the video with retries
        for attempt in range(1, max_retries + 1):
            try:
                # Download the video
                print("Downloading... Please wait.")
                yt_stream.download(output_path=DOWNLOAD_DIR)
                print(f"Download complete! Saved at: {DOWNLOAD_DIR}")
                break  # Exit the loop if download is successful
            except IncompleteRead as e:
                print(f"Retry {attempt}/{max_retries}: IncompleteRead error - {str(e)}")
            except PytubeError as e:
                print(f"PytubeError: {str(e)}")
                break  # Exit the loop if there is an HTTP error that is not an IncompleteRead

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def playlist(link):
    try:
        max_retries = 3

        # Create a YouTube object
        yt_playlist = Playlist(link)

        # Print playlist details
        print(f"Playlist Title: {yt_playlist.title}")
        print(f"Number of Videos in Playlist: {len(yt_playlist.video_urls)}")

        # Iterate through each video in the playlist
        for video in yt_playlist.videos:
            for attempt in range(1, max_retries + 1):
                try:
                    # Download the video with retries
                    print("Downloading... Please wait.")
                    video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path=DOWNLOAD_DIR)
                    print(f"Download of {video.title} complete!")
                    break  # Exit the loop if download is successful
                except IncompleteRead as e:
                    print(f"Retry {attempt}/{max_retries}: IncompleteRead error - {str(e)}")
                except PytubeError as e:
                    print(f"PytubeError: {str(e)}")
                    break  # Exit the loop if there is an HTTP error that is not an IncompleteRead

        print("Download of the entire playlist is complete!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


def main():
    video_type = input("Type s for a single video and p for playlist: ")

    if video_type == "s":
        link = input("Enter the URL of the video to download: ")
        single_video(link)
    elif video_type == "p":
        link = input("Enter the URL of the playlist to download: ")
        playlist(link)
    else:
        print("Invalid option! Please choose either single or playlist.")

if __name__ == "__main__":
    main()