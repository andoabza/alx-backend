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
            if len(self.cache_data) >= self.MAX_ITEMS:
                index = next(iter(self.cache_data))
                self.cache_data.pop(index)
                print(f'DISCARD: {index}')
            self.cache_data.update({key: item})
        return

    def get(self, key):
        '''get value by key'''
        if key:
            return self.cache_data.get(key)
        return None
