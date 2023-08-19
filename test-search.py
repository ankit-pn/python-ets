import os
from elasticsearch import Elasticsearch
# Connect to your ElasticSearch instance
es = Elasticsearch(['http://localhost:9200'])

def search_keywords(keywords):
    search_results = es.search(index="*", body={
        "query": {
            "match": {
                "content": " ".join(keywords)
            }
        }
    })

    # Extract file names, locations, and line numbers from search results
    results = []
    for hit in search_results['hits']['hits']:
        result = {
            'file_name': hit['_source']['file_name'],
            'file_location': hit['_source']['file_location'],
            'line_number': hit['_source']['line_number']
        }
        results.append(result)

    return results

# Example keyword search
keywords_to_search = ["No"]
search_results = search_keywords(keywords_to_search)

# Display search results with line numbers
for result in search_results:
    print(f"File Name: {result['file_name']}, Location: {result['file_location']}, Line Number: {result['line_number']}")
