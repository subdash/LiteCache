import json
import redis
import requests

conn = redis.Redis()


def check_connection(func):
    def inner(*args, **kwargs):
        try:
            conn.ping()
            return func(*args, **kwargs)

        except redis.exceptions.ConnectionError as e:
            print(e)
            print('Suggested remedy: check connection with '
                  '`pgrep redis-server`')

    return inner


@check_connection
def __cache_response(key, data, overwrite=False):
    if conn.exists(key) and not overwrite:
        return

    conn.mset({key: data})


@check_connection
def retrieve(key):
    if conn.exists(key):
        return conn.get(key)

    resp = requests.get(key)
    __cache_response(key, json.dumps(resp.json()))

    return conn.get(key)
