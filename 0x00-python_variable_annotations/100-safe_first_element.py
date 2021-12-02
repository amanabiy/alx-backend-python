#!/usr/bin/env python3
"""
corrected with the right
duck-type annotation
"""
from typing import Sequence, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    The types of the elements of the input are not know
    returns the first element if 1st exist
    other wise returns None
    """
    if lst:
        return lst[0]
    else:
        return None
