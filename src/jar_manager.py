import requests
import settings


jar_url = settings.JOB_SERVER_URI + "jars"

def list_jars():
    r = requests.get(jar_url)
    print r.text
    return json.loads(r.text)

def post_jar(name, jar):
    r = requests.post(jar_url + "/" + name, 
                      data=file(jar, 'rb').read())
    print r.text
    return json.loads(r.text)

def main():
    post_jar("cassandra-test", "/home/spark/spark-examples/casandra_test/target/scala-2.10/SparkCassandraTest-assembly-1.0.jar")
    list_jars()

if __name__ == '__main__':
    main()
