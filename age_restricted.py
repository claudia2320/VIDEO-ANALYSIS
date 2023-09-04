import pandas as pd
from pytube import YouTube

def download_videos_from_excel(file_path):
    df = pd.read_excel(file_path, header=None)  # Assume there are no headers

    for index, row in df.iterrows():
        video_link = row[0]  # Access the first column as there are no headers

        try:
            yt = YouTube(video_link)
            stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
            if stream:
                print(f"Downloading video {yt.title}...")
                stream.download(output_path='videos')
                print(f"Video {yt.title} downloaded successfully.")
            else:
                print(f"Could not find a downloadable stream for video {yt.title}.")
        except Exception as e:
            print(f"An error occurred while downloading the video: {str(e)}")

if __name__ == '__main__':
    excel_file_path = "/Users/claudiamoreno/Desktop/UROP/ANALYSIS/downloads/AGE RESTRICTED VIDEOS/age_restricted_videos.xlsx" 
    download_videos_from_excel(excel_file_path)
