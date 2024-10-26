#!/usr/bin/env python3
"""Module 'web.py' contains function get_page """
from functools import wraps
from typing import Callable
import redis
import requests


store = redis.Redis()


def track_url_access(fn: Callable) -> Callable:
    """Counts the number of times a method is called"""

    @wraps(fn)
    def wrapper(url: str) -> str:
        """Increments call counter, then returns method call"""
        store.incr("count:{}".format(url))
        result = store.get("result:{}".format(url))
        if result:
            return result.decode("utf-8")
        result = fn(url)
        store.set("count:{}".format(url), 0)
        store.setex("result:{}".format(url), 10, result)
        return result

    return wrapper


@track_url_access
def get_page(url: str) -> str:
    """Return the content of a url and
    tracks the number of times it was access and also caches its result"""
    return requests.get(url).text
