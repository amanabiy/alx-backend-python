#!/usr/bin/env python3
"""
Annotating the given function to
return the correct output
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return the correct annotation value """
    return [(i, len(i)) for i in lst]
