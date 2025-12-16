import pytest
from collections import namedtuple
from src.practice.prac000_003 import solution as solution_me


# 공통 테스트 데이터 (namedtuple 사용)
ExampleData = namedtuple(
    "ExampleData",
    [
        "enroll",
        "referral",
        "seller",
        "amount",
        "rates",
        "unit_price",
        "min_forward",
        "expected",
    ],
)

# cspell:disable
TEST_DATA_LIST = [
    ExampleData(
        enroll=["a", "b", "c", "d"],
        referral=["-", "a", "b", "b"],
        seller=["d", "d", "c"],
        amount=[1, 2, 3],
        rates=[0, 20, 30, 40],
        unit_price=100,
        min_forward=5,
        expected=[42, 168, 210, 180],
    )
]
# cspell:enable


# 나의 풀이 테스트
@pytest.mark.parametrize("test_data", TEST_DATA_LIST)
def test_solution_me(test_data: ExampleData):
    """기본 테스트 케이스 검증 - 나의 풀이"""
    enroll, referral, seller, amount, rates, unit_price, min_forward, expected = (
        test_data  # 구조분해(언패킹)
    )
    result = solution_me(
        enroll, referral, seller, amount, rates, unit_price, min_forward
    )
    assert result == expected


# AI 풀이 테스트
# ...
