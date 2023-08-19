from elasticsearch import Elasticsearch

# Connect to your ElasticSearch instance
es = Elasticsearch(['http://localhost:9200'])

# Get a list of all index names
index_names = es.indices.get_alias().keys()

# Delete each index
for index_name in index_names:
    es.indices.delete(index=index_name)

print("All indexes have been deleted.")
