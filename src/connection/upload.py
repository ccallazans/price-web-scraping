import boto3
import datetime
import pandas as pd
import io

BUCKET_NAME = '#'
KEY_NAME = 'price-' + datetime.datetime.now().strftime("%Y-%m-%d") + '.csv'

def upload_file():
    s3_client = boto3.client('s3')
    data = pd.read_csv('/opt/airflow/src/temp/file.csv')

    with io.StringIO() as csv_buffer:
        data.to_csv(csv_buffer, index=False)

        response = s3_client.put_object(
            Body=csv_buffer.getvalue(),
            Bucket=BUCKET_NAME,
            Key=KEY_NAME
        )

    print("Successful Upload!\n")