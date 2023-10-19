#!/usr/bin/env python3
"""
exercise.py
"""
from typing import Union
import redis
import uuid


class Cache:
    """
    This class is a Cache that create an instance of the redis and also
    creates a method stores
    """

    def __init__(self, host='localhost', port=6379, db=0):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        The method stores a data with a random get key
        """

        random_key = uuid.uuid4()
        random_key_str: str = str(random_key)
        self._redis.set(random_key_str, data)
        return random_key_str
