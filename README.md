# Memgraph Data Migration

## Description

This project is designed to facilitate data migration into Memgraph, a high-performance graph database. It provides tools and scripts to import data from dremio into Memgraph.
There is a script extract the data from dremio and automattically insert to the memgraph database based on the pre-defined data model. 

## How to run

by running this script, it will transaction the data from the specificed data base from dremio (following to the query put into the dremio client service) and then it will insert the data into the memgraph database. to start running this, ensure you have installed python. 

1. Git Clone the repository

```bash
git clone https://gitlabuat.ababank.com/SREY.Votana/memgraph-data-migration-application.git
``` 

2. Create the python virtual environment
```bash
python -m venv .venv
``` 

3. Install the dependencies
```bash
pip install -r requirements.txt
``` 

4. Create the .env file
```bash
DREMIO_HOST = "dremio_host"
DREMIO_PORT = "32010"
DREMIO_USER = "user"
DREMIO_PW = "123"
MEMGRAPH_HOST = "memgraph_host"
``` 

5. Run the program 
```bash
python main.py
``` 