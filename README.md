# ETL-Pipeline-with-Apache-Airflow
(i) In Exercise1, we finished the process_web_log data pipeline process with 4 tasks.

(ii) In Exercise2, We did test runs for each of the tasks we defined and a test run for the workflow.Additionally, we triggered the workflow and monitored a few runs. Document the test runs with our findings or observations from the runs.

(iii) In Exercise3, we added to the workflow a task that implemented sending a message to Slack after the last task.

## Author

- **Jintao Ma** - *ETL pipeline* - [Jintao](https://github.com/woshimajintao)
- **Xianyun Zhuang** - *Slack Alarm* - [Xianyun](https://github.com/lisi)

## System Requirements

This project requires the following system environment:
- **Operating System**: Windows 10 or higher
- **Python Version**: Python 3.0 or higher
- **Docker**: Latest version of [Docker](https://www.docker.com/products/docker-desktop) must be installed.
- **Docker Compose**: Required for orchestrating multi-container setups. Typically included with Docker Desktop for Windows and Mac. For Linux, follow the [installation guide](https://docs.docker.com/compose/install/).
- **Airflow**: Stable version of [Airflow](https://airflow.apache.org/docs/apache-airflow/2.7.3/docker-compose.yaml) must be installed.

## Installation

```bash
# Clone the repository to Airflow\dags
git clone https://github.com/woshimajintao/ETL-Pipeline-with-Apache-Airflow.git specific_folder_Airflow\dags
```

## Usage

```bash
# Run the Airflow in the Airflow Folder
docker compose up -d

# Close the Airflow in the Airflow Folder
docker compose down
```


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
