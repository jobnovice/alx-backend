#!/usr/bin/env python3
"""LIFO caching"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFO replacement caching implemented"""
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if key in self.cache_data.keys():
            self.cache_data[f"{key}"] = item
            return
        if len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            print("DISCARD: {}".format(last_key))
            self.cache_data.popitem()
        self.cache_data[f"{key}"] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data[key] if key in self.cache_data.keys() else None
