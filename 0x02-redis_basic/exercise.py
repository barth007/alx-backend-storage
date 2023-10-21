#!/usr/bin/env python3
"""
exercise.py
"""
from typing import Union, Optional, Callable
import redis
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    This is decorator that counts the number times
    a method in the Cache is called
    """

    @wraps(method)
    def wrapper_func(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper_func


def call_history(method: Callable) ->Callable:
    """
    This is a decorator that adds the input and output to a
    redis list
    """

    @wraps(method)
    def wrapper_func(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        inputs = str(args)
        self._redis.rpush(input_key, inputs)
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, result)
        return result
    return wrapper_func


class Cache:
    """
    This class is a Cache that create an instance of the redis and also
    creates a method stores
    """

    def __init__(self, host='localhost', port=6379, db=0):
        self._redis = redis.Redis(host=host, port=port, db=db)
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        The method stores a data with a random get key
        """

        random_key = uuid.uuid4()
        random_key_str: str = str(random_key)
        self._redis.set(random_key_str, data)
        return random_key_str

    def get(self, key: str,
            *fn: Optional[Callable[[str], None]]) -> Union[str, bytes, int]:
        """
        This is a typed annoted method
        """

        if not self._redis.exists(key):
            return None
        value = self._redis.get(key)
        if fn:
            for func in fn:
                value = fn(value)
        return value

    def get_int(self, key: str) -> int:
        """
        This is type annoted method that returns an integer
        """

        return self.get(key, int)

    def get_str(self, key: str) -> str:
        """
        type annoted method that returns an string
        """

        return self.get(key, str)
