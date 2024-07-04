#!/usr/bin/env python3
''' type-annotated function '''


from typing import List


def sum_list(input_list: List[float]) -> float:
    ''' function, annonated'''
    n: float = 0.0
    for i in input_list:
        n += i
    return n
