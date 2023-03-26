# Installation and Running Guide

This guide will help you install and run the UCars application locally on your machine. UCars is a car dealership application built using FastAPI, SQLAlchemy, and Angular.

## Prerequisites

- Python 3.8 or higher
- PostgreSQL 13 or higher 

## Installation

Clone the repository to your local machine

Create a virtual environment and activate it using the following commands:

```shell
python3 -m venv venv
source venv/bin/activate
```

Install the required Python dependencies using the following command:
```shell
pip install -r requirements.txt
```

Create a `.env` file in the root directory of the project and add the following environment variables (copy the values from the `.env.example` file):

Update the environment variable with your PostgreSQL database credentials.

Run the following command to create the database tables and migrate the database
```shell
alembic upgrade head
```

Start the backend server using the following command:
```shell
python main.py
```

Access the application at http://localhost:8000/docs to view the API documentation