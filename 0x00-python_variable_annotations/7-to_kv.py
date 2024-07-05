#!/usr/bin/env python3
""" function to_kv that takes a string k and an int OR float v as arguments and returns a tuple. The first element of the tuple is the string k """


from typing import Union


def to_kv(k: str, v: float) -> tuple:
    ''' function itself '''
    t: tuple
    t = (k, v**2)
    return t
