import os
import frontmatter

def format_folder_name(folder_name):
    """Format folder names like 'code-generation' to 'Code Generation'."""
    return folder_name.replace('-', ' ').title()

def get_markdown_titles(folder_path):
    """Extract titles from markdown files' YAML frontmatter in a given folder."""
    nav_entries = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.md'):
            filepath = os.path.join(folder_path, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
                title = post.get('title', os.path.splitext(filename)[0])  # Default to filename if no title
                nav_entries.append(f"  - {title}: {filename}")  # Indent by 2 spaces for YAML compliance
    return nav_entries

def create_pages_file(folder_path):
    """Create a .pages file in the given folder."""
    folder_name = os.path.basename(folder_path)
    formatted_title = format_folder_name(folder_name)
    
    nav_entries = get_markdown_titles(folder_path)
    
    if nav_entries:
        pages_content = f"title: {formatted_title}\nnav:\n" + "\n".join(nav_entries) + "\n"
        
        pages_filepath = os.path.join(folder_path, '.pages')
        with open(pages_filepath, 'w', encoding='utf-8') as f:
            f.write(pages_content)

def process_directory(root_dir):
    """Recursively process all directories and create .pages files."""
    for dirpath, dirnames, filenames in os.walk(root_dir):
        create_pages_file(dirpath)

# Set the root directory to start processing
root_directory = '/home/daniel/Git/llms-on-llms/docs'

# Run the script
process_directory(root_directory)