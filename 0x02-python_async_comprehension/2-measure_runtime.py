#!/usr/bin/env python3
''' measuring time '''

from typing import List
import time
import asyncio
comp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' function itself'''
    start: float = time.time()

    tasks = [comp() for _ in range(4)]
    res: List[List[float]] = await asyncio.gather(*tasks)

    stop: float = time.time()
    total: float = stop - start

    return total
