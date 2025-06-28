import pytest
from src.lv00.Exam000_000000 import solution


def test_solution__default_test_case_01():
    # 양수 테스트
    assert solution(3, 4) == 7
    assert solution(27, 19) == 46
    assert solution(1, 1) == 2


def test_solution__default_test_case_02_type_error():
    # 타입 에러 테스트
    with pytest.raises(TypeError):
        solution("2", 3)
    with pytest.raises(TypeError):
        solution(4, "5")
