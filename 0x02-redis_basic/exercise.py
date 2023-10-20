#!/usr/bin/env python3
"""
exercise.py
"""
from typing import Union, Optional, Callable
import redis
import uuid


class Cache:
    """
    This class is a Cache that create an instance of the redis and also
    creates a method stores
    """

    def __init__(self, host='localhost', port=6379, db=0):
        self._redis = redis.Redis(host=host, port=port, db=db)
        self._redis.flushdb()

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
        if fn is not None:
            return fn(value)
        else:
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
