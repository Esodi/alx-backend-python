#!/usr/bin/env python3
''' type-annotated function make_multiplier '''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' function itself '''
    def func(multiplier: float) -> float:
        return multiplier * multiplier
    return func
