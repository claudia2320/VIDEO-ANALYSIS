import os

subfolder_name = '/Users/claudiamoreno/Desktop/UROP/ANALYSIS/downloads/AGE RESTRICTED'  # Replace with the actual name of your subfolder

# Get the current working directory
current_directory = os.getcwd()

# Construct the full path of the subfolder
subfolder_path = os.path.join(current_directory, subfolder_name)

# Get a list of all the files in the subfolder
files = os.listdir(subfolder_path)

# Sort the files alphabetically
files.sort()

# Iterate over the files and rename them
for index, file_name in enumerate(files):
    # Generate the new file name with the desired number
    new_file_name = f"{index + 0}.mp4"

    # Construct the full file paths
    original_path = os.path.join(subfolder_path, file_name)
    new_path = os.path.join(subfolder_path, new_file_name)

    # Rename the file
    os.rename(original_path, new_path)

print("Files renamed successfully!")
