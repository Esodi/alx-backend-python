#!/usr/bin/env python3
''' asyncio generator '''


from typing import AsyncGenerator
import asyncio
import random


async def async_generator() -> AsyncGenerator[float, None]:
    ''' the function itself '''
    for i in range(10):
        rand: float = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield rand
