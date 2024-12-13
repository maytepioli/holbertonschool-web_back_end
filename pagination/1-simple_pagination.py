#!/usr/bin/env python3
import csv
from genericpath import getsize
import math
from pydoc import pager
from typing import List


def index_range(page=1, page_size=10):
    """
    Calcula el rango de índices (start, end) que
    corresponden a la página solicitada.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


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
        """
        Recupera un subconjunto de datos correspondiente a
        una página específica
        """
        assert isinstance(pager, int) and page > 0
        assert isinstance(getsize, int) and page_size > 0
        start, end = index_range(page, page_size)
        dataset = self.dataset()
        if start >= len(dataset):
            return []
        return dataset[start:end]
