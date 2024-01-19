#!/usr/bin/env python3
# pylint: disable=missing-docstring

from itertools import chain, pairwise, starmap
from operator import sub

x_values = pairwise(list(map(int, input("enter x values: ").split())))
fx_values = pairwise(list(map(int, input("enter f(x) values: ").split())))


def get_trapezoid(height: int, f1_f2: tuple[int, int]) -> float:
    f1, f2 = f1_f2
    return 1 / 2 * height * (f1 + f2)


heights = list(starmap(sub, tuple(map(reversed, x_values))))
print(sum(list(starmap(get_trapezoid, zip(heights, chain(fx_values))))))
