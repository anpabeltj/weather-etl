

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


from scripts import extract as e
from scripts import transform as t
from scripts import load as l

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1
}

with DAG('weather_pipeline', default_args=default_args, schedule='@daily', catchup=False) as dag:
    def run_extract():
        return e.extract_city("Jakarta")

    def run_transform(**context):
        data = context['ti'].xcom_pull(task_ids='extract_weather_data')
        return t.transform(data, "Jakarta")

    def run_load(**context):
        df = context['ti'].xcom_pull(task_ids='transform_weather_data')
        l.load(df)
    extract_task = PythonOperator(
        task_id='extract_weather_data',
        python_callable=run_extract
    )

    transform_task = PythonOperator(
        task_id='transform_weather_data',
        python_callable=run_transform,
    )

    load_task = PythonOperator(
        task_id='load_weather_data',
        python_callable=run_load
    )



    extract_task >> transform_task >> load_task