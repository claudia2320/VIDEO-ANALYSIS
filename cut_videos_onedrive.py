import os
import pandas as pd
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def cut_video(input_path, output_path, start_time, end_time):
    # This function cuts a video file from the specified start_time to the end_time
    ffmpeg_extract_subclip(input_path, start_time, end_time, targetname=output_path)

# Specify the path to the OneDrive folder
onedrive_folder = "/path/to/OneDrive"

# Specify the subfolder within the OneDrive folder
subfolder = "UROP/ANALYSIS/TOTAL IDIOTS AT WORK 2023_AmazingCompilations"

# Get the full path of the subfolder within the OneDrive folder
subfolder_path = os.path.join(onedrive_folder, subfolder)

# Read data from Excel file in the subfolder
excel_file_path = os.path.join(subfolder_path, "video_cut.xlsx")
data = pd.read_excel(excel_file_path)

# Process each row in the Excel file
for index, row in data.iterrows():
    # Extract the video name, start time, end time, and code from the current row
    video_name = str(row['Video'])
    start_minute = row['Start Minute']
    start_second = row['Start Second']
    end_minute = row['End Minute']
    end_second = row['End Second']
    code = row['Scenario_code (A : workplace, B : road, C : other)']

    # Create the full path of the input video file
    video_file = os.path.join(subfolder_path, video_name + ".mp4")

    # Calculate the start time and end time in seconds
    start_time = start_minute * 60 + start_second
    end_time = end_minute * 60 + end_second

    # Increment the index by 1 to start the output file index from A1
    output_index = index + 1

    # Create the full path of the output file
    output_file = os.path.join(subfolder_path, f"{code}-{output_index}.mp4")

    # Cut the video from the specified start time to the end time and save it as the output file
    cut_video(video_file, output_file, start_time, end_time)
