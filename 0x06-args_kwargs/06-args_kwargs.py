#!/usr/bin/env python3
"""
    * args and ** kwargs
    arguments and keyword arguments
"""


def sum_all(*args, **kwargs):
    """
    args can accept any number of positional arguments
    kwargs can accept any number of keyword-value pair
    """
    print('args: {}'.format(args))
    print('kwargs: {}'.format(kwargs))
    total_kwargs = 0
    for val in kwargs.values():
        total_kwargs += val
    return sum(args, total_kwargs)


print(sum_all(1, 2, 3, 4, 5, n1=10, n2=20, n3=40))
