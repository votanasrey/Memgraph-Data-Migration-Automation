import pandas as pd 
import numpy as np
from utils.helper import get_dremio_data
from dotenv import load_dotenv
load_dotenv()
import os

mg_host = os.getenv('MEMGRAPH_HOST')
print(mg_host)