#!/usr/bin/env python3
"""
web.py
"""
from functools import wraps
from typing import Callable
import requests
import redis


def count(method: Callable) -> Callable:
    """
    This is a decorator that tracks the number of times a
     a url is called
    """

    @wraps(method)
    def wrapper_func(url: str, *args, **kwargs):
        r = redis.Redis('localhost', port=6379, db=0)
        key = f"count:{url}"
        value = r.incr(key)
        expiration_time = 10
        r.setex(key, expiration_time, value)
        count = r.get(key)
        print(f"{key} counts {count.decode('utf-8')} times:")
        return method(url, *args, **kwargs)
    return wrapper_func


@count
def get_page(url: str) -> str:
    """
    This is makes a request to a url and returns
    the content
    """

    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        return content
    return f"requests failed"


get_page('http://slowwly.robertomurray.co.uk')
