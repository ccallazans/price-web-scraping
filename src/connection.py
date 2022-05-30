import boto3
import datetime
import io

BUCKET_NAME = 'BUCKET'
KEY_NAME = 'price-' + datetime.datetime.now().strftime("%Y-%m-%d") + '.csv'

def upload_file(data):
    s3_client = boto3.client('s3')

    with io.StringIO() as csv_buffer:
        data.to_csv(csv_buffer, index=False)

        response = s3_client.put_object(
            Body=csv_buffer.getvalue(),
            Bucket=BUCKET_NAME,
            Key=KEY_NAME
        )

    print("Successful Upload!\n")