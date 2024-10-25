#!/usr/bin/env python3
"""Module 'exercise.py' contains class Cache """
import redis
import uuid
from typing import Union, Callable


class Cache:
    """Represents a cache object for storing data in Redis"""

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores a value in redis and returns the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> None:
        """Gets data using key from redis"""
        data = self._redis.get(key)
        if not fn:
            return data
        return fn(data)

    def get_str(self, key: str) -> str:
        """Gets and decodes to string using get method"""
        return self.get(key, lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Gets and converts to int using get method """
        return self.get(key, lambda x: int(x))
