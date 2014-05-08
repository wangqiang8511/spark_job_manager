import json
import requests
import settings


job_url = settings.JOB_SERVER_URI + "jobs"

def list_jobs(limit=10):
    params = {
        "limit" : limit 
    }
    r = requests.get(job_url, params=params)
    print r.text
    return json.loads(r.text)

def get_job_result(job_id):
    r = requests.get(job_url + "/" + job_id)
    print r.text
    return json.loads(r.text)

def get_job_config(job_id):
    r = requests.get(job_url + "/" + job_id + "/config")
    print r.text
    return json.loads(r.text)

def start_job(app_name, class_path, context, data):
    params = {
        "appName"  : app_name,
        "classPath" : class_path,
        "context" : context,
    }
    r = requests.post(job_url, params=params, data=data)
    print r.text
    return json.loads(r.text)
