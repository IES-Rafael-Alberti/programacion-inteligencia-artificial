from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import ExternalPythonOperator
# Importar las funciones que definiremos más adelante
from data_extraction import extract_data
from data_preprocessing import preprocess_data
from train_model import train_model
from validate_model import validate_model

# https://airflow.apache.org/docs/apache-airflow/stable/howto/operator/python.html#externalpythonoperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 4, 28),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
dag = DAG(
    'iris_ml_workflow',
    default_args=default_args,
    description='A workflow to train and validate'
    'a machine learning model for Iris classification',
    schedule_interval=timedelta(days=1),
)

# Definir las tareas del DAG
pythonPath = '/home/jmsa/miniconda3/envs/torchcartkers/bin/python'
extract_task = ExternalPythonOperator(task_id='extract_data',
                       python_callable=extract_data, dag=dag,python=pythonPath)
preprocess_task = ExternalPythonOperator(task_id='preprocess_data',
                       python_callable=preprocess_data, dag=dag,python=pythonPath)
train_task = ExternalPythonOperator(task_id='train_model',
                       python_callable=train_model, dag=dag,python=pythonPath)
validate_task = ExternalPythonOperator(task_id='validate_model',
                       python_callable=validate_model, dag=dag,python=pythonPath)
# Establecer las dependencias entre las tareas
preprocess_task.set_upstream(extract_task)
train_task.set_upstream(preprocess_task)
validate_task.set_upstream(train_task)

