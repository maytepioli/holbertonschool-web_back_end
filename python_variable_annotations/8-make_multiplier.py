#!/usr/bin/env python3
"""
Devuelve una función que multiplica un número
flotante por el valor de 'multiplier'
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Devuelve una función que multiplica un número
    flotante por el valor de 'multiplier'
    """
    def multiplier_fuction(x: float):
        return x * multiplier
    return multiplier_fuction
