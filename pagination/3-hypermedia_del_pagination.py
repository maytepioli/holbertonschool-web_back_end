#!/usr/bin/env python3
"""
Este archivo contiene una clase y métodos.
"""
import csv
import math
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
        Recupera un subconjunto de datos correspondiente
        a una página específica
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        dataset = self.dataset()
        if start >= len(dataset):
            return []
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns a dictionary of hyperlinks to the given page
        and page size in the given page
        """
        data_set = self.get_page(page, page_size)

        long = len(self.dataset())
        paginas = math.ceil(long / page_size)

        return {
            "page_size": len(data_set),
            "page": page,
            "data": data_set,
            "next_page": page + 1 if page < paginas else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": paginas
        }
