# Introduction

Wrapper for [Spark Job Server](https://github.com/ooyala/spark-jobserver) API in python.

# Interface

* Jar

```python
    post_jar("natasha-game", "/home/spark/NatashGame/target/scala-2.10/NatashaGame-assembly-1.0.jar")
    print list_jars()
```

* Context

```python
    start_context("NatashaGame", mem="2571m")
    stop_context("cassandra-test")
    list_contexts()
```

* Job

```python
    data = """conf {
    s3_access_key=""
    s3_secret_key=""
    s3_path=""
}
""" 
    data2 = """conf {
    game="Forsaken"
}
"""
    start_job("natasha-game", "com.razerzone.NatashaGame.UserGameCacheJob", "NatashaGame", data)
    start_job("natasha-game", "com.razerzone.NatashaGame.GameQueryJob", "NatashaGame", data2)
    list_jobs()
```
