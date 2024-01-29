#!/usr/bin/env python3
import csv
import math
from typing import List


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
        assert isinstance(page, int) and page > 0, "Page must be an integer greater than 0"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be an integer greater than 0"
        start = (page - 1) * page_size
        end = page * page_size
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]