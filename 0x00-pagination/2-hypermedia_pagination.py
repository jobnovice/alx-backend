#!/usr/bin/env python3
"""wrote the module to retreive paginated datasets"""
import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple of size 2 containing the start and end index
    for items on a specific page.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indices.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """intializes the private variable dataset"""
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
        """Returns a list containing paginated dataset."""
        assert (isinstance(page, int) and isinstance(page_size, int))
        assert (page > 0 and page_size > 0)

        start, end = index_range(page, page_size)
        dataset = self.dataset()
        if start >= len(self.dataset()):
            return []

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Return a dict containing information about the pagination."""
        data = self.get_page(page, page_size)
        total_records = len(self.dataset())
        total_pages = (total_records + page_size - 1) // page_size
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
            }
