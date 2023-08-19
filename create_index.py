import os
from elasticsearch import Elasticsearch

# Connect to your ElasticSearch instance
es = Elasticsearch(['http://localhost:9200'])

# Main folder path
main_folder = '/Users/pain/Documents/Projects/python-ets-script/output_text_files'

# Function to traverse the folders and index content
index_name = "transcribe"

def index_content(folder_path):
    count = 0
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith('.txt'):  # Process only text files
                relative_path = os.path.relpath(os.path.join(root, filename), folder_path)
                with open(os.path.join(root, filename), 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                # Index each line with metadata
                for line_number, line_content in enumerate(lines, start=1):
                    unique_id = f"{os.path.basename(root)}_{filename}_line_{line_number}"
                    document = {
                        'content': line_content,
                        'file_name': filename,
                        'file_location': relative_path,  # Store relative file location
                        'line_number': line_number
                    }
                    es.index(index=index_name, id=unique_id, body=document)
                    # print(count)
                    count = count + 1

# Start indexing
index_content(main_folder)
