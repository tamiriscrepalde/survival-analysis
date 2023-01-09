from google.cloud import bigquery
import pandas as pd
import os
from google.cloud import storage


class GoogleUtils():
    """
    Helps with Gooogle Cloud operations
    Args:
        env: enviroment defines if the class will use local key credentials or online credentials
        auth_token_path: path to token to use in local authentication
    """
    def __init__(self):
        self.project_id = os.getenv('GCP_PROJECT_NAME', 'bi-data-science')
        self.init_clients()
        self.default_job_config = bigquery.job.QueryJobConfig(
                use_legacy_sql=False,
                use_query_cache=True
        )
    
    def init_clients(self):
        """
        Init Google Cloud Plataform client services
        """
        self.bq_client = bigquery.Client()


    def read_from_bq(self, query):
        """
        Executes a query on BigQuery and return the result as a pandas dataframe
        Args:
            query: query to execute (SQL Standard)
        Returns:
            query_result: query result as a Pandas Dataframe
        """
        query_job = self.bq_client.query(query, self.default_job_config)
        query_result = query_job.result().to_dataframe()
        return query_result

    def download_blob(self, bucket_name, source_blob_name, destination_file_name):
        """
        Downloads a blob from the bucket.

        Args:
            bucket_name = "your-bucket-name"
            source_blob_name = "local/path/to/file"
            destination_file_name = "storage-object-name"
        """
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(source_blob_name)
        blob.download_to_filename(destination_file_name)


    def upload_blob(self, bucket_name, source_file_name, destination_blob_name):
        """
        Uploads a file to the bucket.
        
        Args:
            bucket_name = "your-bucket-name"
            source_file_name = "local/path/to/file"
            destination_blob_name = "storage-object-name"
        """

        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)

        print(
            "File {} uploaded to {}.".format(
                source_file_name, destination_blob_name
            )
        )
