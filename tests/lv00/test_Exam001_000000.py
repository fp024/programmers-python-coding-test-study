import pytest
from src.lv00.Exam001_000000 import (
    get_lotto,
    get_this_week_lotto,
    print_this_week_lotto,
)


def test_get_lotto():
    lotto = get_lotto(set())
    assert len(lotto) == 6


def test_get_lotto__loop_limit_exceeded():
    with pytest.raises(Exception) as exceptionInfo:
        get_lotto(set(range(1, 45)))

    assert str(exceptionInfo.value) == "루프 반복 제한 한계 도달"


def test_get_this_week_lotto():
    this_week_lotto = get_this_week_lotto()
    assert len(this_week_lotto) == 5


def test_print_this_week_lotto():
    print_this_week_lotto()
