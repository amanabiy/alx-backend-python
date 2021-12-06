#!/usr/bin/env python3
"""
Measure the runtime
return a float
"""
from time import perf_counter
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measures the time """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    finish = perf_counter() - start
    return finish - start
