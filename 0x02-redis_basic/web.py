#!/usr/bin/env python3
"""Module 'web.py' contains function get_page """
from functools import wraps
from typing import Callable
import redis
import requests


store = redis.Redis()


def cache_url(fn: Callable) -> Callable:
    """Counts the number of times a method is called"""

    @wraps(fn)
    def wrapper(url: str) -> str:
        """Increments call counter, then returns method call"""
        count_key = "count:{}".format(url)
        result_key = "result:{}".format(url)
        if store.exists(count_key) and store.exists(result_key):
            store.incr(count_key)
            result = store.get(result_key)
            return result.decode("utf-8")
        result = fn(url)
        store.set(count_key, 1)
        store.setex(result_key, 10, result)
        return result

    return wrapper


@cache_url
def get_page(url: str) -> str:
    """Return the content of a url and
    tracks the number of times it was access and also caches its result"""
    return requests.get(url).text
