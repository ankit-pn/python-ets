# Python ElasticSearch Text Script (ETS)
## Description

This repository contains Python scripts to index transcribed text data into an Elasticsearch engine. The scripts perform various tasks like counting lines, creating and deleting indices, and tokenizing lines for indexing.

## Features
Automated Tokenization: Tokenizes lines in text files and indexes them into Elasticsearch.
Line Counting: Counts the total number of lines in all text files within a directory.
Index Management: Provides options to create and delete indices in Elasticsearch.
Search Testing: Allows you to test the search functionality on the indexed data.

## Requirements
Python 3.x
Elasticsearch 7.x

To install the required Python packages, run:

``` bash
pip install -r requirements.txt
```

## Usage
### 1. Count Total Lines
Run count_total_lines.py to count the total number of lines in all text files within a directory.

```bash
python count_total_lines.py
```

### 2. Preprocessing
Run split_lines_preprocessing.py to tokenize the lines in text files.

```bash 
python split_lines_preprocessing.py
```

### 3. Create Index
Run create_index.py to index the tokenized lines into Elasticsearch.

```bash
python create_index.py
```

### 4. Delete Index
Run delete_index.py to delete all indices in Elasticsearch.

```bash
python delete_index.py
```

### 4. Test Search
Run test-search.py to test the search functionality on the indexed data.

```bash
python test-search.py
```

### 5. Unzip Data
Run unzip.py to unzip and rename the folder containing the text files.

```bash
python unzip.py
```

## License
MIT License