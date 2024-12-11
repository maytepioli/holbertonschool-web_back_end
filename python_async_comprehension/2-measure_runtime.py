#!/usr/bin/env python3
"""
 Ejecuta la función async_comprehension cuatro veces en paralelo
 y mide el tiempo total.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Ejecuta la función async_comprehension cuatro veces en paralelo
    y mide el tiempo total.
    """
    tiempo_inicio = time.perf_counter()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)
    tiempo_final = time.perf_counter()
    tiempo_total = tiempo_final - tiempo_inicio
    return tiempo_total
