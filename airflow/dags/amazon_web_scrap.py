from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

import sys
sys.path.append('/opt/airflow/src')
from connection.utils import verify_urls
from connection.upload import upload_file


default_args = {
    "owner": "airflow",
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "admin@localhost.com",
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

with DAG(
    dag_id='amazon_web_scrap',
    start_date=datetime(2021, 1, 1),
    schedule_interval='@daily',
    default_args=default_args,
    catchup=False
) as dag:

    test_products_links = PythonOperator(
        task_id='test_products_links',
        python_callable=verify_urls
    )

    run_python_script = BashOperator(
        task_id='run_python_script',
        bash_command='python /opt/airflow/src/app.py',
    )

    upload_data_to_s3 = PythonOperator(
        task_id='upload_data_to_s3',
        python_callable=upload_file
    )

    test_products_links >> run_python_script >> upload_data_to_s3