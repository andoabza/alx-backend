#!/usr/bin/env python3
'''a caching system'''
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''last in first out cache'''
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        '''add value pair to the data'''
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                index = list(self.cache_data)[len(self.cache_data) - 1]
                if len(self.cache_data) == self.MAX_ITEMS:
                    self.cache_data.popitem()
                    print(f'DISCARD: {index}')
                    self.cache_data.update({key: item})
                self.cache_data.popitem()
            self.cache_data.update({key: item})
        return

    def get(self, key):
        '''return data by key'''
        if key:
            return self.cache_data.get(key)
        return None
