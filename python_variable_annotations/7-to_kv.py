#!/usr/bin/env python3
"""
funcion retorna una tupla
"""


from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    return (k, v(** 2))
