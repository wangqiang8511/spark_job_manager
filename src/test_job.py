from job_manager import start_job, list_jobs

def main():
    data_format = """
query {
    cassandra_host = "10.0.0.10",
    cassandra_port = "9160",
    date = "%s",
}
""" 
    from datetime import datetime
    for i in range(2, 7):
        t = datetime(2014, 4, i, 0, 0, 0)
        tstr = t.strftime("%Y-%m-%dT%H:%M:%SZ")
        data = data_format % tstr
        res = start_job("cassandra-test",
                  "com.razerzone.SparkCassandraTest.GameSyncCountByDateApi",
                  "cassandra-test",
                  data)
        if res["status"] == "STARTED":
            job_id = res["result"]["jobId"]
            print job_id

    list_jobs()


    pass


if __name__ == '__main__':
    main()
