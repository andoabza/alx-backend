#!/usr/bin/env python3
'''a caching system'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''first in first out cache'''
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        '''add data into dictionary'''
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                index = list(self.cache_data)[0]
                if len(self.cache_data) == self.MAX_ITEMS:
                    self.cache_data.pop(index)
                    print(f"DISCARD: {index}")
                    self.cache_data.update({key: item})
                # self.cache_data.pop(index)
                # print(f"DISCARD: {index}")
            self.cache_data.update({key: item})

        return

    def get(self, key):
        '''return value by key'''
        if key:
            return self.cache_data.get(key)
        return None
