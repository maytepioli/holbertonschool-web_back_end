#!/usr/bin/env python3
"""
    Esta función recibe una lista de números enteros o flotantes, y devuelve
    la suma de esos números como un número flotante.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Esta función recibe una lista de números enteros o flotantes, y devuelve
    la suma de esos números como un número flotante.
    """
    total = sum(mxd_lst)
    return float(total)
