import pytest
import time
import os
import unittest

from tap import TAPTestRunner

from calc import add

parameters = {
    "sum1": (2, 2, 4),
    "sum2": (5, 5, 10),
    "sum3": (3, 2, 7),
    "sum4": (2, -2, 9)
}

params_list = []

for key, value in parameters.items():
    param = pytest.param(*value, id=key)
    params_list.append(param)


@pytest.mark.parametrize("x, y, expected", params_list)
def test_add(x, y, expected):
    assert add(x, y) == expected
    assert add(x, y * -1) == expected * -1
