import os
import pandas as pd
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


def cut_video(input_path, output_path, start_time, end_time):
    # This function cuts a video file from the specified start_time to the end_time
    ffmpeg_extract_subclip(input_path, start_time, end_time, targetname=output_path)


# Get the full path of the subfolder within the current working directory
video_name = "3"
subfolder = "Youtube_videos/Temp/3/"  # Replace with your subfolder name
subfolder_path = os.path.join(os.getcwd(), subfolder)

# Read data from Excel file in the subfolder
excel_file_path = os.path.join(subfolder_path, "3-Scenes.csv")
data = pd.read_csv(excel_file_path, skiprows=1)

# Process each row in the Excel file
for index, row in data.iterrows():
    # Extract the video name, start time, end time, and code from the current row
    scene_number = str(row['Scene Number'])
    start_time = row['Start Time (seconds)']
    end_time = row['End Time (seconds)']

    # Create the full path of the input video file
    video_file = os.path.join(subfolder_path, video_name + ".mp4")

    # Increment the index by 1 to start the output file index from A1
    output_index = index + 1

    # Create the full path of the output file
    output_file = os.path.join(subfolder_path, f"{video_name}-{scene_number}.mp4")

    # Cut the video from the specified start time to the end time and save it as the output file
    cut_video(video_file, output_file, start_time, end_time)


