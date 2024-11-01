#!/usr/bin/env python3
"""LFU Caching"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """LFU cache replacement strategy implemented"""
    def __init__(self):
        """overidden the super init method"""
        super().__init__()
        self.acc_num = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data.keys():
            self.cache_data[f"{key}"] = item
            val = self.acc_num[f"{key}"]
            self.acc_num[f"{key}"] = val + 1
            return
        if len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS:
            lowest = min(list(self.acc_num.values()))
            kei = next((k for k, v in self.acc_num.items() if v == lowest),
                       None)
            self.cache_data.pop(kei)
            self.acc_num.pop(kei)
            print("DISCARD: {}".format(kei))
            self.cache_data[f"{key}"] = item
            self.acc_num[f"{key}"] = 0
            return

        self.cache_data[f"{key}"] = item
        self.acc_num[f"{key}"] = 0

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data.keys():
            val = self.acc_num[f"{key}"]
            self.acc_num[f"{key}"] = val + 1
            return self.cache_data[f"{key}"]
        else:
            return None
