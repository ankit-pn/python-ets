import os

# Define the directory path
directory_path = 'output_text_files'

# Function to count lines in a file
def count_lines(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for line in file)

total_lines = 0

# Traverse through the directory structure
for folder_name in os.listdir(directory_path):
    folder_path = os.path.join(directory_path, folder_name)
    if os.path.isdir(folder_path):
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.txt'):
                file_path = os.path.join(folder_path, file_name)
                num_lines = count_lines(file_path)
                total_lines += num_lines
                print(f"File: {file_name}, Lines: {num_lines}")

print(f"Total lines in all files: {total_lines}")

