import os
import nltk
from nltk.tokenize import sent_tokenize

# Download the punkt tokenizer models
nltk.download('punkt')

# Define input and output directories
input_dir = 'input_text_files'
output_dir = 'output_text_files'

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to process a single text file
def process_text_file(input_path, output_path):
    with open(input_path, 'r') as input_file:
        content = input_file.read()
    
    sentences = sent_tokenize(content)
    
    with open(output_path, 'w') as output_file:
        for sentence in sentences:
            output_file.write(sentence + '\n')

# Process each folder and its files in the input directory
for folder_name in os.listdir(input_dir):
    folder_path = os.path.join(input_dir, folder_name)
    if os.path.isdir(folder_path):
        output_folder_path = os.path.join(output_dir, folder_name)
        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)
        
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.txt'):
                input_file_path = os.path.join(folder_path, file_name)
                output_file_path = os.path.join(output_folder_path, file_name)
                process_text_file(input_file_path, output_file_path)

print("Processing complete.")
