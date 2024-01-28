#!/usr/bin/env python3
''' script that return range of index'''


def index_range(page, pages_size):
    '''return start and end'''
    start = (page - 1) * pages_size
    end = page * pages_size
    return (start, end)
