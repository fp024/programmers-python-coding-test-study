import pytest
from collections import namedtuple
from src.practice.prac000_001 import solution as solution_me

# 공통 테스트 데이터 (namedtuple 사용)
ExampleData = namedtuple("ExampleData", ["nodes", "expected"])

# cspell:disable
TEST_DATA_LIST = [
    ExampleData(
        nodes=[1, 2, 3, 4, 5, 6, 7],
        expected=["1 2 4 5 3 6 7", "4 2 5 1 6 3 7", "4 5 2 6 7 3 1"],
    )
]
# cspell:enable


# 나의 풀이 테스트
@pytest.mark.parametrize("test_data", TEST_DATA_LIST)
def test_solution_me(test_data: ExampleData):
    """기본 테스트 케이스 검증 - 나의 풀이"""
    nodes, expected = test_data  # 구조분해(언패킹)
    result = solution_me(nodes)
    assert result == expected


# AI 풀이 테스트
# ...
