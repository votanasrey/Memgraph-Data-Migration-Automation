import re
import pandas as pd
import dremio_client.lib as dlib


def get_dremio_data(query):
    q = query
    data = dlib.simple_query(q)
    return data