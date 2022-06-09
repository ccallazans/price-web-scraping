from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    "owner": "airflow",
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "admin@localhost.com",
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

with DAG(
    dag_id='amazon-web-scrap',
    start_date=datetime(2021, 1, 1),
    schedule_interval='@daily',
    default_args=default_args,
    catchup=False
) as dag:

    testando = BashOperator(
        task_id='testando',
        bash_command='python /opt/airflow/src/app.py',
    )