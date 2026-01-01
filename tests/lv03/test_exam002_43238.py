from collections import namedtuple

import pytest

from src.lv03.exam002_43238 import solution as solution_me

# 공통 테스트 데이터 (namedtuple 사용)
ExampleData = namedtuple("ExampleData", ["n", "times", "expected"])

# cspell:disable

TEST_DATA_LIST = [
    ExampleData(
        n=6,
        times=[7, 10],
        expected=28,
    )
]

# cspell:enable


# 나의 풀이 테스트
@pytest.mark.parametrize("test_data", TEST_DATA_LIST)
def test_solution_me(test_data: ExampleData):
    """기본 테스트 케이스 검증 - 나의 풀이"""
    n, times, expected = test_data  # 구조분해(언패킹)
    result = solution_me(n, times)
    assert result == expected
