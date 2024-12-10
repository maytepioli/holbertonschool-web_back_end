#!/usr/bin/env python3
"""
Este archivo define la función async_comprehension
que usa un generador asíncrono
para obtener una lista de números aleatorios.
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Este archivo define la función async_comprehension
    que usa un generador asíncrono
    para obtener una lista de números aleatorios.
    """
    return [num async for num in async_generator()]
