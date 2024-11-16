import os

def add_gitkeep_to_empty_folders(base_dir):
    """
    Recursively add .gitkeep files to all empty folders in the given base directory.
    
    :param base_dir: The root directory to start searching for empty folders
    """
    # Walk through the directory tree
    for root, dirs, files in os.walk(base_dir):
        # Check if the current directory is empty (no files and no non-empty subdirectories)
        if not files and not dirs:
            # Create .gitkeep file path
            gitkeep_path = os.path.join(root, '.gitkeep')
            
            # Only create .gitkeep if it doesn't already exist
            if not os.path.exists(gitkeep_path):
                # Create an empty .gitkeep file
                open(gitkeep_path, 'a').close()
                print(f"Added .gitkeep to: {root}")

# Hardcoded directory path
base_dir = '/home/daniel/Git/llms-on-llms'
add_gitkeep_to_empty_folders(base_dir)