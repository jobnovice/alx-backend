#!/usr/bin/env python3
"""Basic dictionary"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """new class that inherits from BaseCaching"""
    def put(self, key, item):
        """ Add an item in the cache
        """
        self.cache_data[f"{key}"] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data[key] if key in self.cache_data.keys() else None
