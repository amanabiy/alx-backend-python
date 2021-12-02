#!/usr/bin/env python3
"""
 a type-annotated function sum_list which takes
 a list input_list of floats as argument and
 returns their sum as a float.
"""


def sum_list(nums: list[float]) -> float:
    """ adds all the numbers in the list and
    returns a float number"""
    return sum(nums)
