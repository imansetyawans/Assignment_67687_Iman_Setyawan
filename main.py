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
    url = 'https://raw.githubusercontent.com/imansetyawans/Assignment_67687_Iman_Setyawan/main/pariwisatabantul.csv'
    datamanca = pd.read_csv(url, error_bad_lines=False)
    wisatamanca = datamanca.loc[:, ['nama_desa_wisata', 'wisatawan_mancanegara']]
    sortwisatamanca = wisatamanca.sort_values(by='wisatawan_mancanegara', ascending = False).head()

    resultA = sortwisatamanca.to_json()
    parsedA = json.loads(resultA)
    json.dumps(parsedA, indent=4)

    return json.dumps(parsedA, indent=4)

@app.get("/wisatanusan")
def show_item():
	
    url = 'https://raw.githubusercontent.com/imansetyawans/Assignment_67687_Iman_Setyawan/main/pariwisatabantul.csv'
    datanusan = pd.read_csv(url, error_bad_lines=False)
    wisatanusan = datanusan.loc[:, ['nama_desa_wisata', 'wisatawan_nusantara']]
    sortwisatanusan = wisatanusan.sort_values(by='wisatawan_nusantara', ascending = False).head()

    resultB = sortwisatanusan.to_json()
    parsedB = json.loads(resultB)
    json.dumps(parsedB, indent=4)

    return json.dumps(parsedB, indent=4)


if __name__== "__main__":
	uvicorn.run(app,host="127.0.0.1",port=int(os.environ.get('PORT',5000)), log_level="info")
