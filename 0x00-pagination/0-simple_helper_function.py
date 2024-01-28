#!/usr/bin/env python3
''' script that return range of index'''
from typing import Tuple


def index_range(page: int, pages_size: int) -> Tuple:
    '''return start and end'''
    start = (page - 1) * pages_size
    end = page * pages_size
    return (start, end)
