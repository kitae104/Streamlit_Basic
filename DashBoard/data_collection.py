# -*- coding:utf-8 -*-
import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

SERVICE_KEY = os.getenv("SEOUL_API_KEY")
# print(SERVICE_KEY)

def main():
  data = None
  for i in range(1, 12):
    url = f"http://openapi.seoul.go.kr:8088/{SERVICE_KEY}/json/tbLnOpendataRtmsV/{1+((i-1)*1000)}/{i*1000}"
    print(url)

    req = requests.get(url)
    content = req.json()
    con = content["tbLnOpendataRtmsV"]["row"]
    result = pd.DataFrame(con)
    data = pd.concat([data, result])

  data = data.reset_index(drop=True)
  data['DEAL_YMD'] = pd.to_datetime(data['DEAL_YMD'], format='%Y%m%d')
  data.to_csv("./data/seoul_real_estate.csv", index=False)

if __name__ == "__main__":
  main()
