import os
import re
import enchant  # PyEnchant library for checking if a word is an English word

# Initialize English dictionary
english_dict = enchant.Dict("en_US")

def is_english_word(word):
    """Check if a word is an English word."""
    return english_dict.check(word)

def process_filename(filename):
    """Process the filename, removing non-English words before .md extension."""
    # Match any string before .md preceded by a hyphen
    match = re.match(r'^(.*?)-([a-zA-Z]+)\.md$', filename)
    
    if match:
        base_name, possible_word = match.groups()
        # If it's not an English word, remove it
        if not is_english_word(possible_word):
            return f"{base_name}.md"
    
    # Return unchanged filename if no match or it's an English word
    return filename

def rename_files_in_directory(directory):
    """Recursively rename files in directory."""
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.md'):
                new_filename = process_filename(filename)
                # If the filename has changed, rename it
                if new_filename != filename:
                    old_path = os.path.join(dirpath, filename)
                    new_path = os.path.join(dirpath, new_filename)
                    print(f"Renaming '{old_path}' to '{new_path}'")
                    os.rename(old_path, new_path)

if __name__ == "__main__":
    docs_dir = "/home/daniel/Git/llms-on-llms/docs"
    rename_files_in_directory(docs_dir)