import pytest
from collections import namedtuple
from src.lv01.exam004_42576 import solution as solution_me

# 공통 테스트 데이터 (namedtuple 사용)
ExampleData = namedtuple("ExampleData", ["participant", "completion", "expected"])

# cspell:disable
TEST_DATA_LIST = [
    ExampleData(
        participant=["leo", "kiki", "eden"],
        completion=["eden", "kiki"],
        expected="leo",
    ),
    ExampleData(
        participant=["marina", "josipa", "nikola", "vinko", "filipa"],
        completion=["josipa", "filipa", "marina", "nikola"],
        expected="vinko",
    ),
    ExampleData(
        participant=["mislav", "stanko", "mislav", "ana"],
        completion=["stanko", "ana", "mislav"],
        expected="mislav",
    ),
]
# cspell:enable


# 나의 풀이 테스트
@pytest.mark.parametrize("test_data", TEST_DATA_LIST)
def test_solution_me(test_data: ExampleData):
    """기본 테스트 케이스 검증 - 나의 풀이"""
    participant, completion, expected = test_data  # 구조분해(언패킹)
    result = solution_me(participant, completion)
    assert result == expected
