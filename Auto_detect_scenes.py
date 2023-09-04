import os
import subprocess

def disassemble_video(video_path, output_directory):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Perform scene detection using scenedetect CLI
    command = f"scenedetect --input {video_path} --output {output_directory} detect-content list-scenes"
    subprocess.call(command, shell=True)

# Example usage
video_path = "Youtube_videos/Temp/3/3.mp4"
output_directory = "Youtube_videos/Temp/3/"
disassemble_video(video_path, output_directory)
