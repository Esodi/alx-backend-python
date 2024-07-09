#!/usr/bin/env python3
''' the asyncio comprehesion '''


from typing import List
import asyncio
import random
gene = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    ''' function itself '''
    lst: List[float] = [i async for i in gene()]
    return lst
