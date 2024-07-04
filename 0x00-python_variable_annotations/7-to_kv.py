#!/usr/bin/env python3
"""type-annotated function to_kv that takes a string k & int or float v as arg and returns tuple. first element of tuple is string k. second element is square of int/float v and should be annotated as a float.
"""

import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """returns a tuple of the string & square of v as float"""
    return (k, float(v * v))
