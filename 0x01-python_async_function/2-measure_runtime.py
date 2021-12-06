#!/usr/bin/env python3
"""
Measure the runtime
return a float
"""
wait_n = __import__('1-concurrent_coroutines').wait_n
import asyncio
import datetime

def measure_time(n: int, max_delay: int) -> float:
    """ Measures the time """
    start = datetime.datetime.now()
    asyncio.run(wait_n(n, max_delay))
    finish = datetime.datetime.now()
    return finish - start
    