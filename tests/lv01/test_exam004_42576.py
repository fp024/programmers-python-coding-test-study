import pytest
from collections import namedtuple
from src.lv01.exam004_42576 import solution as solution_me

# 공통 테스트 데이터 (namedtuple 사용)
TestData = namedtuple("TestData", ["participant", "completion", "expected"])

# cspell:disable
TEST_DATA_LIST = [
    TestData(
        participant=["leo", "kiki", "eden"],
        completion=["eden", "kiki"],
        expected="leo",
    ),
    TestData(
        participant=["marina", "josipa", "nikola", "vinko", "filipa"],
        completion=["josipa", "filipa", "marina", "nikola"],
        expected="vinko",
    ),
    TestData(
        participant=["mislav", "stanko", "mislav", "ana"],
        completion=["stanko", "ana", "mislav"],
        expected="mislav",
    ),
]
# cspell:enable


# 나의 풀이 테스트
@pytest.mark.parametrize("test_data", TEST_DATA_LIST)
def test_solution_me(test_data):
    """기본 테스트 케이스 검증 - 나의 풀이"""
    participant, completion, expected = test_data  # 구조분해(언패킹)
    result = solution_me(participant, completion)
    assert result == expected
