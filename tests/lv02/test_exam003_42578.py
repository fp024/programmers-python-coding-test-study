import pytest
from collections import namedtuple
from src.lv02.exam003_42578 import solution as solution_me

# 공통 테스트 데이터 (namedtuple 사용)
ExampleData = namedtuple("ExampleData", ["clothes", "expected"])
# cspell:disable
TEST_DATA_LIST = [
    ExampleData(
        clothes=[
            ["yellow_hat", "headgear"],
            ["blue_sunglasses", "eyewear"],
            ["green_turban", "headgear"],
        ],
        expected=5,
    ),
    ExampleData(
        clothes=[
            ["crow_mask", "face"],
            ["blue_sunglasses", "face"],
            ["smoky_makeup", "face"],
        ],
        expected=3,
    ),
]
# cspell:enable


# 나의 풀이 테스트
@pytest.mark.parametrize("test_data", TEST_DATA_LIST)
def test_solution_me(test_data: ExampleData):
    """기본 테스트 케이스 검증 - 나의 풀이"""
    clothes, expected = test_data  # 구조분해(언패킹)
    result = solution_me(clothes)
    assert result == expected
