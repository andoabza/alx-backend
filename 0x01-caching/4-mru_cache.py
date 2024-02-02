#!/usr/bin/env python3
'''a caching system'''
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    '''most recently used first out cache'''
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        '''update the data'''
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                keys = list(self.cache_data.keys())
                del self.cache_data[keys[-2]]
                print("DISCARD: {}".format(keys[-2]))
                self.cache_data.update({key: item})

    def get(self, key):
        '''get value by key'''
        if key:
            return self.cache_data.get(key)
        return None