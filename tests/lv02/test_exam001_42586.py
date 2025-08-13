import pytest
from src.lv02.exam001_42586 import solution as solution_me

# 공통 테스트 데이터
TEST_CASES = [
    {"progresses": [93, 30, 55], "speeds": [1, 30, 5], "expected": [2, 1]},
    {
        "progresses": [95, 90, 99, 99, 80, 99],
        "speeds": [1, 1, 1, 1, 1, 1],
        "expected": [1, 3, 2],
    },
]


# 나의 풀이 테스트
@pytest.mark.parametrize("test_data", TEST_CASES)
def test_solution_me(test_data):
    """기본 테스트 케이스 검증"""
    result = solution_me(test_data["progresses"], test_data["speeds"])
    assert result == test_data["expected"]
