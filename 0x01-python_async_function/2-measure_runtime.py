#!/usr/bin/env python3
"""
Measure the runtime
return a float
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measures the time """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    finish = time.perf_counter() - start
    return finish - start
