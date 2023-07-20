#!/usr/bin/env python3

""" A script to create a Cache class """


import redis
import uuid
from typing import Union


class Cache:
    """ Init cache declaration """
    def __init__(self):
        """ Create a init method to store instance of Redis client """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Create a store method to return a string """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
