#!/usr/bin/env python3
# pylint: disable=missing-docstring

from itertools import chain, islice, pairwise, starmap, tee
from operator import sub

x_values = pairwise(list(map(float, input("enter x values: ").split())))
fx_values, fx_values_ = tee(
    chain.from_iterable(
        pairwise(list(map(float, input("enter f(x) values: ").split())))
    ),
    2,
)


def get_trapezoid(height: float, f1: float, f2: float) -> float:
    return 1 / 2 * height * (f1 + f2)


heights = list(starmap(sub, tuple(map(reversed, x_values))))
print(
    sum(
        list(
            starmap(
                get_trapezoid,
                zip(
                    heights,
                    islice(fx_values, 0, None, 2),
                    islice(fx_values_, 1, None, 2),
                ),
            )
        )
    )
)

# 0 2 5 7 8
# 0 4 13 21 23
# 85.5
