import boto3
import datetime
import pandas as pd
import io
import os

BUCKET_NAME = os.environ.get('AWS_S3_BUCKET_NAME')
KEY_NAME = 'price-' + datetime.datetime.now().strftime("%Y-%m-%d") + '.csv'

EXPORT_DATA_PATH = '/opt/airflow/src/temp/file.csv'

def upload_file():
    s3_client = boto3.client('s3')
    data = pd.read_csv(EXPORT_DATA_PATH)

    with io.StringIO() as csv_buffer:
        data.to_csv(csv_buffer, index=False)

        response = s3_client.put_object(
            Body=csv_buffer.getvalue(),
            Bucket=BUCKET_NAME,
            Key=KEY_NAME
        )

    if os.path.exists(EXPORT_DATA_PATH):
        os.remove(EXPORT_DATA_PATH)
    print("Successful Upload!\n")