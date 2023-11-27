from pytube import YouTube, Playlist


DOWNLOAD_DIR = 'c:\\Users\\Chudi\\Downloads'

print("YouTube Downloader")

def single_video(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(output_path=DOWNLOAD_DIR)
    except:
        print("An error has occurred")
    print("Download is completed successfully")

def playlist(link):
    ytPlayList = Playlist(link)
    print(len(ytPlayList.video_urls))
    for video in ytPlayList.videos:
        try:
            video.streams\
                .filter(progressive=True, file_extension='mp4')\
                    .order_by('resolution')\
                        .desc()\
                            .first().download(output_path=DOWNLOAD_DIR)
        except:
            print(f"An error has occurred, {ytPlayList.video_urls} does not exist")
            print(f"Downloading... {len(ytPlayList.video_urls)}")
    print("Playlist is completed successfully")

def Download():
    video_type = input("Is it a single video or a playlist: ")

    if video_type == "single":
        link = input("Enter the URL of the video to download: ")
        single_video(link)
    elif video_type == "playlist":
        link = input("Enter the URL of the playlist to download: ")
        playlist(link)
    else:
        print("Invalid option! Please choose either single or playlist.")


Download()
