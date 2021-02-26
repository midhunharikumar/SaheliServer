from fastapi import FastAPI, File, UploadFile, Form
import tempfile
import os
from dbconnector import MongoConnector, JobScheduler, JobEnumerator, Job
import pandas as pd
import utils
import json
import logging


LOG = logging.getLogger('simple_example')
LOG.setLevel(logging.DEBUG)


app = FastAPI()
mgc = MongoConnector('localhost', 'saheli-prime', 'customer_info')
#mgc_jobs = MongoConnector('localhost', 'jobs_db', 'scheduled')
jobsenum = JobEnumerator()
scheduler = JobScheduler()


@app.post("/files/")
async def create_file(file: bytes=File(...)):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile=File(...)):
    LOG.info("File upload invoked")
    extension = os.path.splitext(file.filename)[1]
    _, path = tempfile.mkstemp(prefix='parser_', suffix=extension)
    LOG.info("tmp file at: {}".format(path))
    with open(path, 'wb') as f:
        f.write(file.file.read())
    return {"filename": file.filename, "path": path}


@app.post("/addcustomer/")
async def create_customer(details: str):
    LOG.info('Add customer invoked !')
    dict_data = json.loads(details)
    print(dict_data)
    return "Its not caching period"


@app.get("/showcustomers/")
async def show_customers():
    customers = mgc.get_all()
    # customers = pd.DataFrame(customers)
    # print(customers)
    return customers


@app.post("/schedulejob/")
async def schedulejob(job):
    LOG.info('scheduling a Job')
    scheduler.create(job)


@app.post("/claim_job/")
async def claim_job(job_id: str=Form(...), provider_id: str=Form(...)):
    scheduler.update({"_id": job_id}, {"claim_status": True,
                                       "claim_provider": provider_id})
    LOG.info('Claiming job')


@app.get("/showjobs/")
async def show_jobs():
    LOG.info('Showing Jobs')
    jobs = jobsenum.get_jobs()
    return jobs


@app.get("/health")
async def health():
    return "healthy"
