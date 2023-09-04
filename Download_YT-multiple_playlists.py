from pytube import YouTube, Playlist
import os
import openpyxl

def download_youtube_video(video_url, folder_path):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Check if the video requires age confirmation
        if yt.age_restricted:
            print(f"Age confirmation required for: {yt.title}. Skipping download.")
            write_to_excel(video_url)
            return  # Skip downloading for age-restricted videos

        video = yt.streams.get_highest_resolution()

        # Create the subfolder if it doesn't exist
        os.makedirs(folder_path, exist_ok=True)

        # Download the video into the subfolder
        video.download(output_path=folder_path)

        print(f"Download completed for: {yt.title}")
    except Exception as e:
        print(f"An error occurred for: {video_url}\nError: {str(e)}")

def write_to_excel(video_url):
    excel_path = os.path.join(os.getcwd(), "age_restricted_videos.xlsx")

    if not os.path.isfile(excel_path):
        workbook = openpyxl.Workbook()
        workbook.save(excel_path)

    workbook = openpyxl.load_workbook(excel_path)
    sheet = workbook.active

    row = [video_url]
    sheet.append(row)

    workbook.save(excel_path)

def download_playlist_videos(playlist_url, folder_path):
    try:
        playlist = Playlist(playlist_url)
        videos = playlist.video_urls

        for video_url in videos:
            download_youtube_video(video_url, folder_path)

    except Exception as e:
        print(f"An error occurred while downloading playlist videos.\nError: {str(e)}")

# List of YouTube playlist URLs
playlist_urls = [
    "https://www.youtube.com/playlist?list=PLefeXMTcE0-sQLYV4FCP-U2HcDq4dElnT",
    "https://www.youtube.com/playlist?list=PLefeXMTcE0-sv_bUHqh29UhyVKaHg5Rlq",
    "https://www.youtube.com/playlist?list=PLU3Wu7yxCQbZsrPbkI5bG4_YHfS0QlYr3",
    "https://www.youtube.com/playlist?list=PLs-nV9_SwNpcLNW7mv_bk4hGYHmBMhCIx"
    # Add more playlist URLs as needed
]

# Provide the desired subfolder name within the current folder
subfolder_name = "downloads"

for playlist_url in playlist_urls:
    # Get the full path of the subfolder
    folder_path = os.path.join(os.getcwd(), subfolder_name, playlist_url.split('=')[-1])

    # Download videos from the playlist
    download_playlist_videos(playlist_url, folder_path)
