import pandas as pd
import json
import re
import requests
import urllib3
from bs4 import BeautifulSoup


url="https://api.846policebrutality.com/api/incidents?include=evidence"

http = urllib3.PoolManager()
response = http.request('GET', url)
soup = BeautifulSoup(response.data, "html.parser")

json_846 = json.loads(soup.text)
incidents = json_846['data']


df_846 = pd.DataFrame(incidents)

df_846.to_csv('df_846.csv')







