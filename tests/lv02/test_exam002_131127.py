import pytest
from collections import namedtuple
from src.lv02.exam002_131127 import solution as solution_me

# 공통 테스트 데이터 (namedtuple 사용)
TestData = namedtuple("TestData", ["want", "number", "discount", "expected"])
# cspell:disable
TEST_DATA_LIST = [
    TestData(
        want=["banana", "apple", "rice", "pork", "pot"],
        number=[3, 2, 2, 2, 1],
        discount=[
            "chicken",
            "apple",
            "apple",
            "banana",
            "rice",
            "apple",
            "pork",
            "banana",
            "pork",
            "rice",
            "pot",
            "banana",
            "apple",
            "banana",
        ],
        expected=3,
    ),
    TestData(
        want=["apple"],
        number=[10],
        discount=[
            "banana",
            "banana",
            "banana",
            "banana",
            "banana",
            "banana",
            "banana",
            "banana",
            "banana",
            "banana",
        ],
        expected=0,
    ),
]
# cspell:enable


# 나의 풀이 테스트
@pytest.mark.parametrize("test_data", TEST_DATA_LIST)
def test_solution_me(test_data: TestData):
    """기본 테스트 케이스 검증 - 나의 풀이"""
    want, number, discount, expected = test_data  # 구조분해(언패킹)
    result = solution_me(want, number, discount)
    assert result == expected
