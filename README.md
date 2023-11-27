# ETL-Pipeline-with-Apache-Airflow
- **Exercise1**:We finished the process_web_log data pipeline process with 4 tasks.

- **Exercise2** :We did test runs for each of the tasks we defined and a test run for the workflow.Additionally, we triggered the workflow and monitored a few runs. Document the test runs with our findings or observations from the runs.

- **Exercise3** :We added to the workflow a task that implemented sending a message to Slack after the last task.

## Contributors

- **Jintao Ma** - *ETL Pipeline* - [Jintao](https://github.com/woshimajintao)
- **Xianyun Zhuang** - *Slack Message* - [Xianyun](https://github.com/zhuangxianyun)

## System Requirements

This project requires the following system environment:
- **Operating System**: Windows 10 or higher
- **Python Version**: Python 3.0 or higher
- **Docker**: Latest version of [Docker](https://www.docker.com/products/docker-desktop) must be installed.
- **Docker Compose**: Required for orchestrating multi-container setups. Typically included with Docker Desktop for Windows and Mac. For Linux, follow the [installation guide](https://docs.docker.com/compose/install/).
- **Airflow**: Stable version of [Airflow](https://airflow.apache.org/docs/apache-airflow/2.7.3/docker-compose.yaml) needs to be installed.

## Docker Setup

- **Install Docker**: Visit [Docker's website](https://www.docker.com/products/docker-desktop) to download and install Docker Desktop for Windows or Mac. For Linux users, install Docker Engine following the instructions provided on the Docker website.

- **Verify Docker Installation**: After installation, run `docker --version` in your command line to verify that Docker has been installed successfully.

- **Install Docker Compose (if not included)**: For Windows users, if Docker Compose is not already included, follow the official [Docker Compose installation guide](https://docs.docker.com/compose/install/).

- **Verify Docker Compose Installation**: Run `docker-compose --version` to ensure it is installed correctly.


## Usage
To run the application using Docker and Docker Compose, follow these steps:


```bash
# Clone the repository to the folder of ..Aiflow\dags
git clone https://github.com/woshimajintao/ETL-Pipeline-with-Apache-Airflow.git specific_folder_Airflow\dags

# Navigate to the project directory
cd ..Airflow\dags

# Build and run the containers
docker-compose up -d

# Close the Airflow in the Airflow Folder
docker compose down
```


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
