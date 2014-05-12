import json
import requests
import settings


def get_context_url(host):
    return host + "contexts"

def list_contexts(host=settings.JOB_SERVER_URI):
    r = requests.get(get_context_url(host))
    print r.text
    return json.loads(r.text)

def start_context(name, cpu=4, mem="512m", host=settings.JOB_SERVER_URI):
    params = {
        "num-cpu-cores" : str(cpu),
        "memory-per-node" : mem,
    }
    r = requests.post(get_context_url(host) + "/" + name, params=params)
    print r.text

def stop_context(name, host=settings.JOB_SERVER_URI):
    r = requests.delete(get_context_url(host) + "/" + name)
    print r.text
