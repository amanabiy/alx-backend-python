#!/usr/bin/env python3
"""
runs wait_random n times with max_delay as max
return the list of all the delays (float values).
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay) -> List[float]:
    """ runs wait_random n times with max_delay as max """
    all_delays: List = []
    for i in range(n):
        num: float = await wait_random(max_delay)
        all_delays.append(num)
    return all_delays
