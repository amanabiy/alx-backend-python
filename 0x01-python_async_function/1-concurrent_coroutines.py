#!/usr/bin/env python3
"""
runs wait_random n times with max_delay as max
return the list of all the delays (float values).
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ runs wait_random n times with max_delay as max """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
