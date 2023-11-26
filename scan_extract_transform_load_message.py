from datetime import datetime, timedelta
from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

from airflow.hooks.base_hook import BaseHook
import requests


class SlackHook(BaseHook):
    def __init__(self, slack_hook_conn_id='slack_hook', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.slack_hook_conn_id = slack_hook_conn_id

    def get_conn(self):
        conn = self.get_connection(self.slack_hook_conn_id)
        return conn

    def send_message(self, message):
        conn = self.get_conn()
        slack_webhook_url = conn.host
        slack_data = {'text': message}
        response = requests.post(
            slack_webhook_url, json=slack_data,
            headers={'Content-Type': 'application/json'}
        )
        return response

def send_slack_message():
    slack_hook = SlackHook(slack_hook_conn_id='slack')
    slack_hook.send_message('Workflow was executed successfully!')


default_args = {
    'owner': 'Jintao',
    'depends_on_past': False,
    'start_date': datetime(2023, 11, 18),
    'email': ['Mars19990123@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='process_web_log',
    start_date=datetime(2023, 11, 18),
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    catchup=False,
) as dag:
    # Define a FileSensor task
    scan_for_file = FileSensor(
        task_id='scan_for_file',
        filepath='/opt/airflow/dags/the_logs/log.txt',  
        fs_conn_id='my-file-system',  
        timeout=300,  
        mode='poke',  
        poke_interval=60,  
    )

    extract_data = BashOperator(
        task_id='extract_data',
        bash_command='grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}" /opt/airflow/dags/the_logs/log.txt > /opt/airflow/dags/the_logs/extracted_data.txt',
        dag=dag
    )

    transform_data = BashOperator(
        task_id='transform_data',
        bash_command="sed '/198.46.149.143/d' /opt/airflow/dags/the_logs/extracted_data.txt> /opt/airflow/dags/the_logs/transformed_data.txt",
        #bash_command='awk \'$1 != "198.46.149.143"\' /opt/airflow/dags/the_logs/extracted_data.txt > /opt/airflow/dags/the_logs/transformed_data.txt',
        dag=dag
    )

    load_data = BashOperator(
        task_id='load_data',
    #   bash_command='tar -czvf weblog.tar /opt/airflow/dags/the_logs/transformed_data.txt',
        bash_command='tar -rvf /opt/airflow/dags/the_logs/weblog.tar -C /opt/airflow/dags/the_logs/ transformed_data.txt',
        dag=dag
    )

    send_message_task = PythonOperator(
        task_id='send_slack_message',
        python_callable=send_slack_message,
    )

    scan_for_file >> extract_data >> transform_data >> load_data >> send_message_task
