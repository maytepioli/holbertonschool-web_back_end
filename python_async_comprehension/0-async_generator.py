#!/usr/bin/env python3
import random
import asyncio

async def async_generator():
    for i in range(11):
        await asyncio.sleep(1)
        num: float = random.uniform(0, 10)
        yield num
