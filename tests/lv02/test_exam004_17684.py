import pytest
from collections import namedtuple
from src.lv02.exam004_17684 import solution as solution_me

# 공통 테스트 데이터 (namedtuple 사용)
ExampleData = namedtuple("ExampleData", ["msg", "expected"])
# cspell:disable
TEST_DATA_LIST = [
    ExampleData(
        msg="KAKAO",
        expected=[11, 1, 27, 15],
    ),
    ExampleData(
        msg="TOBEORNOTTOBEORTOBEORNOT",
        expected=[20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34],
    ),
    ExampleData(
        msg="ABABABABABABABAB",
        expected=[1, 2, 27, 29, 28, 31, 30],
    ),
]
# cspell:enable


# 나의 풀이 테스트
@pytest.mark.parametrize("test_data", TEST_DATA_LIST)
def test_solution_me(test_data: ExampleData):
    """기본 테스트 케이스 검증 - 나의 풀이"""
    msg, expected = test_data  # 구조분해(언패킹)
    result = solution_me(msg)
    assert result == expected
