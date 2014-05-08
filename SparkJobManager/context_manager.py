import json
import requests
import settings


context_url = settings.JOB_SERVER_URI + "contexts"

def list_contexts():
    r = requests.get(context_url)
    print r.text
    return json.loads(r.text)

def start_context(name, cpu=4, mem="512m"):
    params = {
        "num-cpu-cores" : str(cpu),
        "memory-per-node" : mem,
    }
    r = requests.post(context_url + "/" + name, params=params)
    print r.text

def stop_context(name):
    r = requests.delete(context_url + "/" + name)
    print r.text