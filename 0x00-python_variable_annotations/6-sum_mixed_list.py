#!/usr/bin/env python3
"""type annotated function sum_mixed_list which takes a list mxd_list of integers and floats and returns sum as float"""

import typing

def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """Returns sum of list as float"""
    return float(sum(mxd_lst))
