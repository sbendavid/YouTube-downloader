from pytubefix import YouTube, Playlist
import os

DOWNLOAD_DIR = 'c:\\Users\\samue\\OneDrive\\Downloads'

def download_video_pytubefix(link):
    try:
        yt = YouTube(link)
        
        # Ask user for desired resolution
        available_streams = yt.streams.filter(progressive=True, file_extension='mp4')
        print("Available resolutions:")
        for stream in available_streams:
            print(f"{stream.resolution} - itag: {stream.itag}")
        
        itag = input("Enter the itag of the desired resolution: ")
        selected_stream = yt.streams.get_by_itag(itag)
        
        # Download video
        selected_stream.download(output_path=DOWNLOAD_DIR)
        print(f"Video download completed: {yt.title}")
        
        # Download subtitles if available
        if 'en' in yt.captions:
            caption = yt.captions['en']
            caption_file = os.path.join(DOWNLOAD_DIR, f"{yt.title}_captions.srt")
            with open(caption_file, "w", encoding="utf-8") as f:
                f.write(caption.generate_srt_captions())
            print(f"Subtitles downloaded: {caption_file}")
        else:
            print("No English subtitles available.")
            
    except Exception as e:
        print(f"An error occurred while downloading the video: {e}")

def download_playlist_pytubefix(link):
    try:
        playlist = Playlist(link)
        playlist_dir = os.path.join(DOWNLOAD_DIR, playlist.title)
        if not os.path.exists(playlist_dir):
            os.makedirs(playlist_dir)

        print(f"Downloading playlist: {playlist.title}")
        for index, video in enumerate(playlist.videos, start=1):
            print(f"Downloading video {index}: {video.title}")
            
            # Ask for resolution for each video
            available_streams = video.streams.filter(progressive=True, file_extension='mp4')
            print("Available resolutions:")
            for stream in available_streams:
                print(f"{stream.resolution} - itag: {stream.itag}")
            
            itag = input(f"Enter the itag of the desired resolution for '{video.title}': ")
            selected_stream = video.streams.get_by_itag(itag)
            
            # Download video
            selected_stream.download(output_path=playlist_dir, filename=f"{index} - {video.title}.mp4")
            print(f"Downloaded {video.title}")
            
            # Download subtitles if available
            if 'en' in video.captions:
                caption = video.captions['en']
                caption_file = os.path.join(playlist_dir, f"{index} - {video.title}_captions.srt")
                with open(caption_file, "w", encoding="utf-8") as f:
                    f.write(caption.generate_srt_captions())
                print(f"Subtitles downloaded: {caption_file}")
            else:
                print("No English subtitles available.")
                
        print("Playlist download completed!")
        
    except Exception as e:
        print(f"An error occurred while downloading the playlist: {e}")

def main():
    video_type = input("Type 's' for a single video and 'p' for a playlist: ")

    if video_type == "s":
        link = input("Enter the URL of the video to download: ")
        download_video_pytubefix(link)
    elif video_type == "p":
        link = input("Enter the URL of the playlist to download: ")
        download_playlist_pytubefix(link)
    else:
        print("Invalid option! Please choose either 's' for single video or 'p' for playlist.")

if __name__ == "__main__":
    main()
