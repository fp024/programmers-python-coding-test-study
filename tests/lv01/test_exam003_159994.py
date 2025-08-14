import pytest
from collections import namedtuple
from src.lv01.exam003_159994 import solution as solution_me


# 공통 테스트 데이터 (namedtuple 사용)
TestData = namedtuple("TestData", ["cards1", "cards2", "goal", "expected"])

TEST_DATA_LIST = [
    TestData(
        cards1=["i", "drink", "water"],
        cards2=["want", "to"],
        goal=["i", "want", "to", "drink", "water"],
        expected="Yes",
    ),
    TestData(
        cards1=["i", "water", "drink"],
        cards2=["want", "to"],
        goal=["i", "want", "to", "drink", "water"],
        expected="No",
    ),
]


# 나의 풀이 테스트
@pytest.mark.parametrize("test_data", TEST_DATA_LIST)
def test_solution_me(test_data):
    """기본 테스트 케이스 검증 - 나의 풀이"""
    cards1, cards2, goal, expected = test_data  # 구조분해(언패킹)
    result = solution_me(cards1, cards2, goal)
    assert result == expected
