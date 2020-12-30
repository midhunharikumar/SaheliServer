from fastapi import FastAPI, File, UploadFile
import tempfile
import os
from dbconnector import MongoConnector
import pandas as pd
import utils
app = FastAPI()
mgc = MongoConnector('10.0.0.102:27017')


@app.post("/files/")
async def create_file(file: bytes=File(...)):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile=File(...)):
    extension = os.path.splitext(file.filename)[1]
    _, path = tempfile.mkstemp(prefix='parser_', suffix=extension)
    print(path)
    with open(path, 'wb') as f:
        f.write(file.file.read())
    return {"filename": file.filename, "path": path}


@app.post("/addcustomer/")
async def create_customer(details: str):
    dict_data = json.loads(details)
    print(dict_data)
    return "Its not caching period"


@app.get("/showcustomers/")
async def show_customers():
    customers = mgc.get_all_customer()
    #customers = pd.DataFrame(customers)
    # print(customers)
    return customers


@app.get("/health")
async def health():
    return "healthy"
