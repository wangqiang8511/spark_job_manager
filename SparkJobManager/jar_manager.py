import json
import requests
import settings


def get_jar_url(host):
    return host + "jars"

def list_jars(host=settings.JOB_SERVER_URI):
    r = requests.get(get_jar_url(host))
    print r.text
    return json.loads(r.text)

def post_jar(name, jar, host=settings.JOB_SERVER_URI):
    r = requests.post(get_jar_url(host) + "/" + name, 
                      data=file(jar, 'rb').read())
    print r.text
