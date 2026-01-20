from collections import namedtuple

import pytest

from src.lv03.exam003_42861 import solution as solution_me

# 공통 테스트 데이터 (namedtuple 사용)
ExampleData = namedtuple("ExampleData", ["n", "costs", "expected"])

# cspell:disable
TEST_DATA_LIST = [
    ExampleData(
        n=4,
        costs=[[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]],
        expected=4,
    ),
]
# cspell:enable


# 나의 풀이 테스트
@pytest.mark.parametrize("test_data", TEST_DATA_LIST)
def test_solution_author(test_data: ExampleData):
    """기본 테스트 케이스 검증 - 나의 풀이"""
    n, costs, expected = test_data  # 구조분해(언패킹)
    result = solution_me(n, costs)
    assert result == expected
