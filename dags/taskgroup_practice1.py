from airflow.utils.task_group import TaskGroup
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(
    'basic_task_group',
    schedule_interval='@daily',
    start_date=datetime(2022, 1, 1),
    catchup=False
    ) as dag:

    t0 = EmptyOperator(task_id='start')

    # Start Task Group definition
    with TaskGroup(group_id='group1') as tg1:
        t1 = EmptyOperator(task_id='task1')
        t2 = EmptyOperator(task_id='task2')
        t1 >> t2
    # End Task Group definition

    t3 = EmptyOperator(task_id='end')

    # Set Task Group's (tg1) dependencies
    t0 >> tg1 >> t3