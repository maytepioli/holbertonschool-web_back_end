#!/usr/bin/env python3
"""
funcion asincrónica
"""
import random
import asyncio


async def wait_random(max_delay: int 10) -> float:
    """
    funcion asincrónica
    """
    num: float = random.uniform(0, max_delay)
    await asyncio.sleep(num)
    return num
