#!/usr/bin/env python3
""" function to_kv that takes a string k """

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' function itself '''
    return (k, float(v ** 2))
