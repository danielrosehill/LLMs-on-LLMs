import os

def remove_citations(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    updated_lines = []
    for line in lines:
        if 'Citations:' in line:
            break 
        updated_lines.append(line)
    
    with open(file_path, 'w') as file:
        file.writelines(updated_lines)

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith('.md'):  
                remove_citations(file_path)

# Replace with your directory path
directory_path = '/home/daniel/Git/llms-on-llms'
process_directory(directory_path)