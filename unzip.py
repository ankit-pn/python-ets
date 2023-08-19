import zipfile
import os
import shutil

# Define the paths
zip_file_path = 'transcribe.zip'
extracted_folder_name = 'transcribe'
output_folder_name = 'input_text_files'

# Extract the contents of the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall()

# Rename the extracted folder
if os.path.exists(extracted_folder_name):
    os.rename(extracted_folder_name, output_folder_name)

print(f"Contents of '{zip_file_path}' have been extracted and renamed to '{output_folder_name}' folder.")
