#!/usr/bin/env python3
"""Module 'exercise.py' contains class Cache """
import redis
import uuid
from typing import Union


class Cache:
    """Represents a cache object for storing data in Redis"""

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores a value in redis and returns the key"""
        key = uuid.uuidv4()
        self._redis.set(key, data)
        return key
