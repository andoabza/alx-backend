#!/usr/bin/env python3
'''a caching system'''
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''least recently used first out cache'''
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        '''update the data using LRU'''
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    self.cache_data.pop(key)
                else:
                    index = list(self.cache_data)[0]
                    self.cache_data.pop(index)
                    print(f'DISCARD: {index}')
            self.cache_data.update({key: item})            

    def get(self, key):
        '''get value by key'''
        if key:
            return self.cache_data.get(key)
        return None
