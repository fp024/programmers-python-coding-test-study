from random import random


def get_lotto(prev_set: set):
    if len(prev_set) >= 45 - 6:
        raise Exception("6개의 숫자를 선택할 수 없음")
    lotto = set()
    while len(lotto) < 6:
        lotto_number = int(random() * 45) + 1
        if lotto_number in prev_set:
            continue
        else:
            lotto.add(lotto_number)
    return lotto


def get_this_week_lotto():
    this_week_lotto = []
    init_set = set()

    while len(this_week_lotto) < 5:
        l = get_lotto(init_set)
        init_set.update(l)
        this_week_lotto.append(sorted(l))
    return this_week_lotto


def print_this_week_lotto():
    this_week_lotto = get_this_week_lotto()
    print("\n=== 이번주 로또 번호 ===")
    for index, slot in enumerate(this_week_lotto):
        print(f"slot{index + 1}: ", end="")
        for number in slot:
            print(f"{number:02d}", end=" ")
        print()
