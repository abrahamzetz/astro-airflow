from airflow import DAG
from datetime import datetime

from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator


with DAG("check_dag", 
         start_date=datetime(2023, 1, 1),
         schedule='@daily',
         catchup=False,
         description="DAG to check data",
         tags = ['data_engineering']
         ) as dag:
    
    create_file = BashOperator(
        task_id='create_file',
        bash_command=' echo "Hi there!" >/tmp/dummy'
    )

    check_file_exists = BashOperator(
        task_id='check_file_exists',
        bash_command='test -f /tmp/dummy'
    )

    read_file = PythonOperator(
        task_id='read_file',
        python_callable=lambda: print(open('/tmp/dummy', 'rb').read())
    )

    create_file >> check_file_exists >> read_file