#!/usr/bin/env python3
import csv
import math
from typing import List, Tuple


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
        """return a list containing paginated dataset"""

        assert (isinstance(page, int) and isinstance(page_size, int))
        assert (page > 0 and page_size > 0)
        page, page_size = index_range(page, page_size)
        with open(self.DATA_FILE) as f:
            reader = csv.reader(f)
            dataset = [row for row in reader]
            if page > len(dataset) or page_size > len(dataset):
                return []
            self.__dataset = dataset[page+1:page_size+1]
        return self.__dataset
