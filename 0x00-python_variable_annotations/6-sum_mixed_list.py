#!/usr/bin/env python3
"""
a type-annotated function sum_mixed_list
which takes a list mxd_lst of integers
and floats and  returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(nums: List[Union[int, float]]) -> float:
    """
    accepts both integers and floats in the list and
    returns the sum of the elements as float
    """
    return sum(nums)
