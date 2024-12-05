#!/usr/bin/env python3
"""
funcion retorna una tupla
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    funcion retorna una tupla
    """
    return (k, float(v**2))
