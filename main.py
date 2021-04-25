import pandas as pd
#from typing import optional
from fastapi import FastAPI
import uvicorn
import json
import numpy as np
import os

app = FastAPI()


# @app.get("/wisatanusan")
# def show_item():
#     datanusan = pd.read_csv('Copy of 26. urusan pariwisata.xlsx - 26.11.csv')
#     wisatanusan = datanusan.loc[:, ['nama_desa_wisata', 'wisatawan_nusantara']]
#     sortwisatanusan = wisatanusan.sort_values(by='wisatawan_nusantara', ascending = False).head()

#     B = pd.DataFrame(sortwisatanusan)

#     return B.to_string()

@app.get("/wisatamanca")
def show_item():
    url = 'https://github.com/imansetyawans/Assignment_67687_Iman_Setyawan/blob/main/Copy%20of%2026.%20urusan%20pariwisata.xlsx%20-%2026.11.csv'
    datamanca = pd.read_csv('url, index_col=0)
    wisatamanca = datamanca.loc[:, ['nama_desa_wisata', 'wisatawan_mancanegara']]
    sortwisatamanca = wisatamanca.sort_values(by='wisatawan_mancanegara', ascending = False).head()

    resultA = sortwisatamanca.to_json()
    parsedA = json.loads(resultA)
    json.dumps(parsedA, indent=4)

    return json.dumps(parsedA, indent=4)

@app.get("/wisatanusan")
def show_item():
    datanusan = pd.read_csv('https://github.com/imansetyawans/Assignment_67687_Iman_Setyawan/blob/main/Copy%20of%2026.%20urusan%20pariwisata.xlsx%20-%2026.11.csv')
    wisatanusan = datanusan.loc[:, ['nama_desa_wisata', 'wisatawan_nusantara']]
    sortwisatanusan = wisatanusan.sort_values(by='wisatawan_nusantara', ascending = False).head()

    resultB = sortwisatanusan.to_json()
    parsedB = json.loads(resultB)
    json.dumps(parsedB, indent=4)

    return json.dumps(parsedB, indent=4)


if __name__== "__main__":
	uvicorn.run(app,host="127.0.0.1",port=int(os.environ.get('PORT',5000)), log_level="info")
