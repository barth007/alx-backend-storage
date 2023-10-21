#!/usr/bin/env python3
"""
web.py
"""
from functools import wraps
from typing import Callable
import requests
import redis

r = redis.Redis('localhost', port=6379, db=0)


def count(method: Callable) -> Callable:
    """
    This is a decorator that tracks the number of times a
     a url is called
    """

    @wraps(method)
    def wrapper_func(url: str):
        key = f"count:{url}"
        value = r.incr(key)
        print(f"{key} counts {value} times:")
        return method(url)
    return wrapper_func


@count
def get_page(url: str) -> str:
    """
    This is makes a request to a url and returns
    the content
    """

    response = requests.get(url)
    if response.status_code == 200:
        content: str = response.text
        expiration_time = 10
        r.setex(url, expiration_time, content)
        contents = r.get(url)
        if contents is not None:
            return contents.decode('utf-8')
        else:
            return f"content expired"
    failed_fetch: str = f" requests failed"
    return failed_fetch


if __name__ == "__main__":
    print(get_page('http://slowwly.robertomurray.co.uk'))
