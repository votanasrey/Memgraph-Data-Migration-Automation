import pandas as pd 
import numpy as np
from utils.helper import get_dremio_data
from utils.memgraph_service import memgraph_service

mg_service = memgraph_service() 

print("Querying the dataset ...")

query = '''Query here '''
data = get_dremio_data(query)
data = pd.DataFrame(data) 

print("Dataframe ...")
print(data.head())
print(data.info())

print("Calling Memgraph Service ...")
print(mg_service)

print("Inserting the transaction data into Memgraph ...")

for index, row in data.iterrows():
    transaction = row.to_dict()
    if transaction['CIF_CREATION_DATE'] is not None:
        transaction['CIF_CREATION_DATE'] = transaction['CIF_CREATION_DATE'].strftime('%Y-%m-%d')
    transaction = {k: v if pd.notnull(v) else None for k, v in transaction.items()}
    print(transaction)
    mg_service.create_transaction(transaction)


print("Transaction has been inserted ...")
