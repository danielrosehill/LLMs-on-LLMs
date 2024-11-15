import os
import re

# Define the directory path
folder_path = '/home/daniel/Git/llms-on-llms/outputs/unsorted'

# Iterate over all files in the folder
for filename in os.listdir(folder_path):
    # Construct the full file path
    old_file_path = os.path.join(folder_path, filename)

    # Skip if it's not a file
    if not os.path.isfile(old_file_path):
        continue

    # Replace spaces with hyphens, convert to lowercase, and remove numbers
    new_filename = re.sub(r'\d', '', filename.replace(' ', '-').lower())

    # Construct the new file path
    new_file_path = os.path.join(folder_path, new_filename)

    # Rename the file if the name has changed
    if old_file_path != new_file_path:
        os.rename(old_file_path, new_file_path)
        print(f'Renamed: {old_file_path} -> {new_file_path}')