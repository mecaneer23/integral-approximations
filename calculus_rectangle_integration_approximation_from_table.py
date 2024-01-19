#!/usr/bin/env python3
# pylint: disable=missing-docstring

from itertools import islice, pairwise, starmap, tee
from operator import mul, sub

x_values = pairwise(list(map(int, input("enter x values: ").split())))
right_fx_values, left_fx_values = tee(
    map(int, input("enter f(x) values: ").replace("−", "-").split()), 2
)

heights = list(starmap(sub, tuple(map(reversed, x_values))))
print("left", sum(list(starmap(mul, zip(heights, left_fx_values)))))
print("right", sum(list(starmap(mul, zip(heights, islice(right_fx_values, 1, None))))))
