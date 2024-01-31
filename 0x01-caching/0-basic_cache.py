#!/usr/bin/env python3
'''a caching system'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''basic cache'''
    def put(self, key, item):
        '''method to update chache'''
        if key and item:
            self.cache_data.update({key: item})
        return

    def get(self, key):
        '''method to get by key'''
        if key:
            return self.cache_data.get(key)
        return None
