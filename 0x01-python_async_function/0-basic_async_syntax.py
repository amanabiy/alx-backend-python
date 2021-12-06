#!/usr/bin/env python3
"""
wait random generates randum number
and waits for that number and
return the value
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ generate random number """
    num = random.random() * max_delay
    await asyncio.sleep(num)
    return num
