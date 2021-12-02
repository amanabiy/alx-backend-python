#!/usr/bin/env python3
"""
 a type-annotated function make_multiplier that takes a float multiplier
 as argument and returns a function that multiplies a float by multiplier.
"""


def make_multiplier(multiplier: float) -> function:
    """
    takes a float multiplier
    as argument and returns a function that multiplies a float by multiplier.
    """
    def multiply(multiplier: float, x: float) -> float:
        """ multiplies two numbers """
        return x * multiplier
    return multiply
