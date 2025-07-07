import pytest
from src.lv01.exam001_68644 import solution


def test_solution__default_test_case_01():
    assert solution([2, 1, 3, 4, 1]) == [2, 3, 4, 5, 6, 7]
    assert solution([5, 0, 2, 7]) == [2, 5, 7, 9, 12]
