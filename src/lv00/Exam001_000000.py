from random import random


def get_lotto(prev_set: set):
    loop_limit = 10_000
    lotto = set()
    while len(lotto) < 6:
        lotto_number = int(random() * 45) + 1
        if lotto_number in prev_set:
            continue
        else:
            lotto.add(lotto_number)
        loop_limit -= 1
        if loop_limit == 0:
            raise Exception("루프 반복 제한 한계 도달")
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
