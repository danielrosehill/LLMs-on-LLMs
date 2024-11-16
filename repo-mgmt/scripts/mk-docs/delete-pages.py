import os

def delete_pages_files(directory):
    # Walk through the directory recursively
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.pages'):
                # Create the full path of the file
                file_path = os.path.join(root, file)
                # Delete the file
                os.remove(file_path)
                print(f'Deleted: {file_path}')

# Specify the directory
directory = '/home/daniel/Git/llms-on-llms/docs'

# Call the function to delete .pages files
delete_pages_files(directory)