#!/usr/bin/env python3
"""Module 'exercise.py' contains class Cache """
import redis
import uuid
from typing import Union, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Counts the number of times a method is called"""

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """Increments call counter, then returns method call"""
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, *kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Store the input and output of a method call"""

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> str:
        """Stores the input and output of method call and returns
        the output"""
        input_key = "{}:inputs".format(method.__qualname__)
        output_key = "{}:outputs".format(method.__qualname__)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(output_key, output)
        return output

    return wrapper()


class Cache:
    """Represents a cache object for storing data in Redis"""

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
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
        """Gets and converts to int using get method"""
        return self.get(key, lambda x: int(x))
