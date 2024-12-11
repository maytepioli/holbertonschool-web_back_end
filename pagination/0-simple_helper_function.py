#!/usr/bin/env python3
"""
 Calcula el rango de índices (start, end) que
 corresponden a la página solicitada.
"""


def index_range(page=1, page_size=10):
    """
    Calcula el rango de índices (start, end) que
    corresponden a la página solicitada.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
