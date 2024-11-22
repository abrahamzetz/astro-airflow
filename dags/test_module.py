# test_module.py
from airflow.decorators import dag, task
import pendulum
from my_packages.packages_a.module_a import TestClass
from my_packages.packages_a.subpackage_a.subpackaged_module_a import SubpackagedTestClass

@dag(schedule = None, start_date = pendulum.datetime(2023, 3, 1), catchup = False)
def test_module():

    @task
    def test_task():
        print(f'Hellotime: {TestClass.my_time()}')

    @task
    def sub_test_task():
        print(SubpackagedTestClass.my_time())

    test_task() >> sub_test_task()

dag = test_module()