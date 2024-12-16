#!/usr/bin/env python3
"""
This file contains a class and methods
"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Calculate the range of indexes for paginating data.

    Arguments:
        page (int): Page number (starts at 1).
        page_size (int): Number of elements per page.

    Returns:
        tuple[int, int]: A tuple containing the initial index (inclusive)
        and the final (unique) index for the requested page.
    """
    start = (page - 1) * page_size
    # Calcula el índice inicial de la página ajustando la numeración de páginas
    # (que empieza en 1) a índices basados en 0.

    end = start + page_size
    # Calcula el índice final como el límite exclusivo,
    # sumando el inicio y el tamaño de la página.

    tupla = (start, end)
    return tupla


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
        Returns a specific page of data from the dataset.

        Arguments:
            page (int): The page number to retrieve
            (1-based index). Defaults to 1.
            page_size (int): The number of items per page.
            Defaults to 10.

        Returns:
            List[List]: A list of rows (data) corresponding
            to the requested page.
            If the page is out of range (e.g.,
            requesting a page beyond the available data),
            returns an empty list.
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
