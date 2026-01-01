from collections import namedtuple

import pytest

from src.lv03.exam001_42892 import solution as solution_me

# 공통 테스트 데이터 (namedtuple 사용)
ExampleData = namedtuple("ExampleData", ["nodeinfo", "expected"])

# cspell:disable

TEST_DATA_LIST = [
    ExampleData(
        nodeinfo=[
            [5, 3],
            [11, 5],
            [13, 3],
            [3, 5],
            [6, 1],
            [1, 3],
            [8, 6],
            [7, 2],
            [2, 2],
        ],
        expected=[[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]],
    )
]

# cspell:enable


# 나의 풀이 테스트
@pytest.mark.parametrize("test_data", TEST_DATA_LIST)
def test_solution_me(test_data: ExampleData):
    """기본 테스트 케이스 검증 - 나의 풀이"""
    nodeinfo, expected = test_data  # 구조분해(언패킹)
    result = solution_me(nodeinfo)
    assert result == expected
