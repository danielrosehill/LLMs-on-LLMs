import os

def generate_file_tree(startpath):
    with open('llms-repo.md', 'w') as f:
        for root, dirs, files in os.walk(startpath):
            # Exclude dot folders
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            # Exclude dot files and keep only .md files
            files = [file for file in files if not file.startswith('.') and file.endswith('.md')]
            
            # Calculate the depth of the current directory
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * level  # Indentation for directories
            
            # Write directory name to the file
            f.write(f'{indent}{os.path.basename(root)}/\n')
            
            # Indentation for files
            subindent = ' ' * 4 * (level + 1)
            
            # Write each .md file to the file tree
            for file in files:
                f.write(f'{subindent}{file}\n')

# Path to the repository
repo_path = '/home/daniel/Git/llms-on-llms'

# Generate the file tree and output to llms-repo.md
generate_file_tree(repo_path)