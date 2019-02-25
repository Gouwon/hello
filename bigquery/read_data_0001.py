from google.cloud import bigquery

## if doesn't work, do export command on cli. export GOOGLE_APPLICATION_CREDENTIALS="/Users/mac/workspace/hello/bigquery/bigquery.json"

client = bigquery.Client()

# Perform a query.
QUERY = ('select * from bqdb.Test order by songno')
query_job = client.query(QUERY)  # API request
rows = query_job.result()        # Waits for query to finish

for row in rows:
    print(row)



