import pytest
from src.lv01.exam002_42840 import solution


def test_solution__default_test_case_01():
    assert solution([1, 2, 3, 4, 5]) == [1]
    assert solution([1, 3, 2, 4, 2]) == [1, 2, 3]


def test_solution__extra_test_case_01():
    assert solution([5, 1, 1]) == [2, 3]
