# Prompt

> I'm trying to use a local LLM to do some text classification on a folder in my local computer. I'd like the LLM to iterate over the files in the folder and either identify which of those are tech tutorials or move the files into a subfolder. What's the easiest way to make this work?

# Output

To use a **local LLM** for text classification over a folder of files (markdown files in your case), and then identify and move the tech tutorials into a subfolder, you can follow this approach:

### Approach Overview

1. **Use a Python script** to:
   - Iterate over the markdown files in a folder.
   - Send the content of each file to the local LLM for classification.
   - Based on the model's output (e.g., "Tech Tutorial" or "Other"), move the files into respective subfolders.

### Steps to Implement the Solution

#### 1. Set Up the Local LLM

Since you are running a local LLM (e.g., **LLaMA**, **GPT-J**, or another model) via **LM Studio** or a similar platform, you can interface with the model via Python or through its command-line interface.

- Ensure that you have the model running locally and that you can interact with it programmatically (using Python or a web API).

#### 2. Write the Python Script for File Processing

Here’s how you can build the Python script to classify files and move them:

##### a. Import Required Libraries

First, you'll need some basic Python libraries for file handling and interacting with your LLM:

```python
import os
import shutil
from transformers import AutoTokenizer, AutoModelForCausalLM

# Define paths
source_folder = '/path/to/your/markdown/folder'
tutorials_folder = '/path/to/your/subfolder/for/tutorials'
others_folder = '/path/to/your/subfolder/for/others'

# Ensure the folders exist
os.makedirs(tutorials_folder, exist_ok=True)
os.makedirs(others_folder, exist_ok=True)

# Load your local model (adjust based on your model choice and LLM setup)
model_name = "EleutherAI/gpt-j-6B"  # Or any model you are using
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
model.to("cuda")  # If running on a GPU
```

##### b. Iterate Over Files and Send Content to the Model

Next, create a loop to read each markdown file and pass its content to the LLM for classification:

```python
# Function to classify a document as Tech Tutorial or Other
def classify_file(file_content):
    prompt = "Is this markdown file a technical setup guide? Answer 'Tech Tutorial' or 'Other':\n\n"
    inputs = tokenizer(prompt + file_content, return_tensors="pt").to("cuda")
    
    outputs = model.generate(inputs.input_ids, max_length=100)
    classification = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return "Tech Tutorial" if "Tech Tutorial" in classification else "Other"

# Iterate through the markdown files in the source folder
for file_name in os.listdir(source_folder):
    if file_name.endswith(".md"):  # Process only markdown files
        file_path = os.path.join(source_folder, file_name)
        
        # Read the file content
        with open(file_path, 'r') as file:
            file_content = file.read()

        # Classify the file
        classification = classify_file(file_content)
        
        # Move the file based on the classification
        if classification == "Tech Tutorial":
            shutil.move(file_path, os.path.join(tutorials_folder, file_name))
            print(f"Moved {file_name} to Tech Tutorials folder.")
        else:
            shutil.move(file_path, os.path.join(others_folder, file_name))
            print(f"Moved {file_name} to Others folder.")
```

##### c. Run the Script

Once the script is ready:

- Run it in your terminal or Python environment.
- The script will classify each file based on its content and move it to the appropriate folder.


### Summary

- You can classify markdown files by sending their content to a local LLM (e.g., GPT-J, LLaMA) and processing the model’s responses.
- Once classified, the script automatically moves the files into subfolders for easy organization.
- This approach leverages Python for automation and an LLM for text classification.

Let me know if you need further guidance on setting up the script or optimizing the LLM interaction!

*The above text was generated by a large language model (LLM) and its accuracy has not been validated. This page is part of 'LLMs-on-LLMs,' a Github repository by Daniel Rosehill which explores how curious humans can use LLMs to better their understanding of LLMs and AI. However, the information should not be regarded as authoritative and given the fast pace of evolution in LLM technology will eventually become deprecated. This footer was added at 16-Nov-2024.*


