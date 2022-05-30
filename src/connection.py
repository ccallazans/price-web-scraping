import boto3
import datetime
import io

def upload_file(data):
    s3_client = boto3.client('s3')

    file_name = 'price-' + datetime.datetime.now().strftime("%Y-%m-%d") + '.csv'

    with io.StringIO() as csv_buffer:
        data.to_csv(csv_buffer, index=False)

        response = s3_client.put_object(
            Body=csv_buffer.getvalue(),
            Bucket='BUCKET',
            Key=file_name
        )

    print("Successful Upload!\n")