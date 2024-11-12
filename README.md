# CampUnix Admin API

REST API for CampUnix administration.

## Prerequisites
- 🐍 Python 3.11.0
- 🌐 Pyenv
- 🐘 PostgreSQL

## Setup Steps for macOS

- **Install Pyenv 3.11.0**  
  ```shell
  pyenv install 3.11.0
  ```

- **Navigate to the Project Directory**  
  ```shell
  cd {project_path}/campunix-admin-api
  ```

- **Enable Pyenv**  
  ```shell
  pyenv local 3.11.0
  eval "$(pyenv init -)"
  ```

- **Create a Virtual Environment**  
  ```shell
  python -m venv .venv
  ```

- **Activate the Virtual Environment**  
  ```shell
  source .venv/bin/activate
  ```

- **Install Poetry**  
  ```shell
  pip install poetry
  ```

- **Install Dependencies**  
  ```shell
  poetry install
  ```

- **Run Alembic Migration**  
  ```shell
  alembic upgrade head
  ```

- **Seed the Database**  
  ```shell
  python -m db_seed.seeder
  ```
