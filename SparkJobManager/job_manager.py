import json
import requests
import settings


def get_job_url(host):
    return host + "/jobs"

def list_jobs(limit=10, host=settings.JOB_SERVER_URI):
    params = {
        "limit" : limit 
    }
    r = requests.get(get_job_url(host), params=params)
    print r.text
    return json.loads(r.text)

def get_job_result(job_id, host=settings.JOB_SERVER_URI):
    r = requests.get(get_job_url(host) + "/" + job_id)
    print r.text
    return json.loads(r.text)

def get_job_config(job_id, host=settings.JOB_SERVER_URI):
    r = requests.get(get_job_url(host) + "/" + job_id + "/config")
    print r.text
    return json.loads(r.text)

def start_job(app_name, class_path, context, data, host=settings.JOB_SERVER_URI):
    params = {
        "appName"  : app_name,
        "classPath" : class_path,
        "context" : context,
    }
    r = requests.post(get_job_url(host), params=params, data=data)
    print r.text
    return json.loads(r.text)
