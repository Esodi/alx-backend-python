#!/usr/bin/env python3
""" function’s parameters and return values """


from typing import List, Tuple, Sequence


def element_length(lst: List[Sequence]) -> List[Tuple[int, Sequence]]:
    ''' Function itself '''
    return [(i, len(i)) for i in lst]
