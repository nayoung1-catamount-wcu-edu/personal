import pandas as pd
import requests
import urllib
from sqlalchemy import create_engine

params = urllib.parse.quote_plus(
    r"Driver={SQL Server Native Client 11.0};"
    r"Server=BARAD-DUR;"
    r"Database=Endeavor;"
    r"trusted_connection=yes;"
    r"fast_executemany=True;"
)

engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)


url = "https://ebscer.com/collegehockey/api/201-2011.json"


data = pd.json_normalize(pd.read_json(requests.get(url).text)["games"])

data.to_sql("hockey_stats", engine, if_exists="append", index=False)
