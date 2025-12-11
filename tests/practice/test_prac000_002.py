import pytest
from collections import namedtuple
from src.practice.prac000_002 import solution as solution_me


# 공통 테스트 데이터 (namedtuple 사용)
ExampleData = namedtuple("ExampleData", ["lst", "search_lst", "expected"])

# cspell:disable
TEST_DATA_LIST = [
    ExampleData(
        lst=[1],
        search_lst=[1],
        expected=[True],
    ),
    ExampleData(
        lst=[1, 2, 3],
        search_lst=[1, 2, 3],
        expected=[True, True, True],
    ),
    ExampleData(
        lst=[5, 3, 8, 4, 2, 1, 7, 10],
        search_lst=[1, 2, 5, 6],
        expected=[True, True, True, False],
    ),
    ExampleData(
        lst=[1, 3, 5, 7, 9],
        search_lst=[2, 4, 6, 8, 10],
        expected=[False, False, False, False, False],
    ),
]
# cspell:enable


# 나의 풀이 테스트
@pytest.mark.parametrize("test_data", TEST_DATA_LIST)
def test_solution_me(test_data: ExampleData):
    """기본 테스트 케이스 검증 - 나의 풀이"""
    lst, search_lst, expected = test_data  # 구조분해(언패킹)
    result = solution_me(lst, search_lst)
    assert result == expected


# AI 풀이 테스트
# ...
