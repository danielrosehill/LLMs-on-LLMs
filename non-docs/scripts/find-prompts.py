import os
import csv

# Base directory to search
base_dir = '/home/daniel/Git/llms-on-llms'

# Output CSV file location
output_csv = '/home/daniel/Git/prompts.csv'

# List to hold the extracted prompts
prompts = []

# Walk through the directory and subdirectories
for dirpath, _, filenames in os.walk(base_dir):
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)
        # Check if the file is of a readable type (e.g., text, markdown, or Python files)
        if filename.endswith(('.txt', '.md', '.py')):
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    lines = file.readlines()
                    for line in lines:
                        # Check if the line starts with one of the specified headings
                        if line.startswith('# Prompt') or line.startswith('## Prompt') or line.startswith('### Prompt'):
                            # Get the relative path of the file
                            rel_path = os.path.relpath(file_path, base_dir)
                            # Append the file name and relative path to the list
                            prompts.append((filename, rel_path))
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")

# Write the results to a CSV file
try:
    with open(output_csv, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        # Write header row
        writer.writerow(['File Name', 'Relative Path'])
        # Write all collected prompts
        writer.writerows(prompts)
    print(f'Prompts written to {output_csv}')
except Exception as e:
    print(f"Error writing to CSV: {e}")