#!/bin/bash

# Define the directory to search
DIRECTORY="/home/daniel/Git/llms-on-llms/docs"

# Define the correct footer text (escaped for use in sed)
FOOTER="---
*The above text was generated by a large language model (LLM) and its accuracy has not been validated. This page is part of 'LLMs-on-LLMs,' a Github repository by Daniel Rosehill which explores how curious humans can use LLMs to better their understanding of LLMs and AI. However, the information should not be regarded as authoritative and given the fast pace of evolution in LLM technology will eventually become deprecated. This footer was added at 16-Nov-2024.*
---"

# Step 1: Replace existing footers
find "$DIRECTORY" -name "*.md" -exec sed -i '/---/,/---/c\
---\
*The above text was generated by a large language model (LLM) and its accuracy has not been validated. This page is part of "LLMs-on-LLMs," a Github repository by Daniel Rosehill which explores how curious humans can use LLMs to better their understanding of LLMs and AI. However, the information should not be regarded as authoritative and given the fast pace of evolution in LLM technology will eventually become deprecated. This footer was added at 16-Nov-2024.*\
---' {} +

# Step 2: Add footer if none exists
find "$DIRECTORY" -name "*.md" -exec bash -c '
if ! grep -q "\*\The above text was generated by a large language model (LLM)" "$1"; then
    echo -e "\n$FOOTER" >> "$1"
fi' _ {} \;