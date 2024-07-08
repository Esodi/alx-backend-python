#!/usr/bin/env python3
''' concurrent gathering asyncio '''


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    ''' function itself '''
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    sorted_results = sorted(results)
    return sorted_results
