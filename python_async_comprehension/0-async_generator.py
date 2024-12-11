#!/usr/bin/env python3
"""
Este script contiene un generador asíncrono que produce
números aleatorios flotantes
entre 0 y 10 cada segundo. El generador usa `asyncio`
para hacer las pausas de manera
asíncrona, lo que permite que otros procesos
continúen ejecutándose mientras se espera.
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Este script contiene un generador asíncrono que produce
    números aleatorios flotantes
    entre 0 y 10 cada segundo. El generador usa `asyncio`
    para hacer las pausas de manera
    asíncrona, lo que permite que otros procesos
    continúen ejecutándose mientras se espera.
    """
    for i in range(10):
        await asyncio.sleep(1)
        num = random.uniform(0, 10)
        yield num
