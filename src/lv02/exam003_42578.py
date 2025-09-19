##################################################################################
# 의상 - 42578
#   - https://school.programmers.co.kr/learn/courses/30/lessons/42578
#
##################################################################################


def solution(clothes: list[list[str]]):

    clothes_dict = {}
    for [_, clothes_type] in clothes:
        # 💡 항목별로 수만 세면 된다.
        clothes_dict[clothes_type] = clothes_dict.get(clothes_type, 0) + 1

    count_mul = 1
    for v in clothes_dict.values():
        count_mul = count_mul * (v + 1)

    return count_mul - 1


if __name__ == "__main__":
    print(
        solution(
            [
                ["yellow_hat", "headgear"],
                ["blue_sunglasses", "eyewear"],
                ["green_turban", "headgear"],
            ],
        )
    )
    print(
        solution(
            [
                ["crow_mask", "face"],
                ["blue_sunglasses", "face"],
                ["smoky_makeup", "face"],
            ],
        )
    )


### 검토 ###
# 일단 조합의 수만 구하는 것이라서 문제가 어려워지진 않는다. (특정 형식으로 출력을 요구하면 그때는 어려워짐)
# 💡 조합의 수 공식
#   (A유형의 의상 갯수 + 1) * (B유형의 의상 갯수 + 1) * ... (n유형의 의상 갯수 + 1) - 1
#   ✔️ 각 의상 개수는 하나씩 입을 경우의 수
#   ✔️ 위에서 + 1을 해준 경우는 안입은 경우의 수
#   ✔️ 마지막에 -1을 해준 것은... 아무것도 안입은 경우의 수를 뺌
