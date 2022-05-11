"""
https://www.codewars.com/kata/52ceafd1f235ce81aa00073a/train/python
"""
import pytest


def plural(n):
    return n != 1


@pytest.mark.parametrize("number, expected_bool", [(0, True),
                                                   (1, False),
                                                   (100, True),
                                                   (1.0, False)])
def test_plural(number, expected_bool):
    assert plural(number) == expected_bool
