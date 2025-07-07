import pytest
from src.lv00.exam001_000000 import (
    get_lotto,
    get_this_week_lotto,
    print_this_week_lotto,
)


def test_get_lotto():
    lotto = get_lotto(set())
    assert len(lotto) == 6


def test_get_lotto__cannot_select_enough_numbers():
    with pytest.raises(ValueError) as exceptionInfo:
        get_lotto(set(range(1, 40)))

    assert str(exceptionInfo.value) == "6개의 숫자를 선택할 수 없음"


def test_get_this_week_lotto():
    this_week_lotto = get_this_week_lotto()
    assert len(this_week_lotto) == 5


def test_print_this_week_lotto():
    print_this_week_lotto()
