#!/usr/bin/env python3
""" type-annotated function sum_mixed_list which takes a list mxd_lst """


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    ''' fuction itself'''
    tot: float = sum(mxd_lst)
    return tot
