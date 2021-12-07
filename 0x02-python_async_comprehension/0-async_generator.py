#!/usr/bin/env python3
"""
The coroutine will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10. Use the random module.
"""
import random
from typing import Generator
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """ loops ten times and yield a random number between 0 and 10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
