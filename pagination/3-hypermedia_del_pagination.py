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
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns resilient paginated data with metadata.

        Args:
            index (int): Starting index.
            page_size (int): Number of items per page.

        Returns:
            dict: Contains the page data and metadata.
        """
        dataset = self.indexed_dataset()
        dataset_size = len(dataset)
        assert index <= dataset_size
        next_index = index + page_size
        if next_index >= dataset_size:
            next_index = None
        data = [
            dataset.get(i)
            for i in range(index, min(index + page_size, dataset_size))
            if dataset.get(i) is not None
        ]
        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index
        }
