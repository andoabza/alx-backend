#!/usr/bin/env python3
'''a class that act as server for pagination'''
import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''return start and end'''
        assert isinstance(page, int) and page > 0, \
            "Page must be an integer greater than 0"
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size must be an integer greater than 0"
        start = (page - 1) * page_size
        end = page * page_size
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        '''get values as dict'''
        assert isinstance(page, int) and page > 0, \
            "Page must be an integer greater than 0"
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size must be an integer greater than 0"
        total = len(self.dataset())
        pages = math.ceil(total / page_size)
        data = self.get_page(page, page_size)
        next_page = page + 1 if page < pages else None
        prev_page = page - 1 if page > 1 else None
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': pages
            }
