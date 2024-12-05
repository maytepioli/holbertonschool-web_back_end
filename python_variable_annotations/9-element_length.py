#!/usr/bin/env python3
"""
 Esta función recibe una lista (o cualquier tipo de iterable)
 de secuencias y devuelve una lista de tuplas
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Esta función recibe una lista (o cualquier tipo de iterable)
    de secuencias y devuelve una lista de tuplas
    """
    return [(i, len(i)) for i in lst]
