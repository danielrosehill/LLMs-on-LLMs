import os
import re

directory = '/home/daniel/git/llms-on-llms'

pattern = re.compile(r'\[\d+\]')

def process_markdown_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    new_content = re.sub(pattern, '', content)

    with open(file_path, 'w') as file:
        file.write(new_content)


for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            process_markdown_file(file_path)

print("Bracketed numbers removed from all markdown files.")