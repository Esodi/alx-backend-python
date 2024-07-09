#!/usr/bin/env python3
''' asyncio generator '''


from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, str, None]:
    for i in range(10):
        await asyncio.sleep(1)
        rand = random.uniform(0, 10)
        yield rand
