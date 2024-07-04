#!/usr/bin/env python3
"""type-annotated function sum_list that takes a list input_list of floats as arg and returns their sum as float
"""

from typing import List

def sum_list(input_list: List[float]) -> float:
    """returns sum as float"""
    return float(sum(input_list))
