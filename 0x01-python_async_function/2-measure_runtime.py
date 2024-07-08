#!/usr/bin/env python3
''' measuring time '''


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' function itself '''
    async def measure(n: int, max_delay: int) -> float:
        ''' inner function '''
        start = time.time()
        await wait_n(n, max_delay)
        end = time.time()

        total = end - start
        return total / n
    return asyncio.run(measure(n, max_delay))
