#!/usr/bin/env python3
"""FIFO caching"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """implemented FIFO cache replacement policy"""
    def __init__(self):
        """intilaizes the object"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if key in self.cache_data.keys():
            self.cache_data[f"{key}"] = item
            return
        if len(self.cache_data.values()) >= BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            print("DISCARD: {}".format(first_key))
            self.cache_data.pop(first_key)
        self.cache_data[f"{key}"] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data[key] if key in self.cache_data.keys() else None
