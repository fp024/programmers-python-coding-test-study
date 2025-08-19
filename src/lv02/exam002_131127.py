##################################################################################
# 할인 행사 - 131127
#   - https://school.programmers.co.kr/learn/courses/30/lessons/42586
#
##################################################################################


def solution(want: list[str], number: list[int], discount: list[str]) -> int:
    # 사야할 물건의 총 수량
    total_amount = sum(number)

    last_start_no = len(discount) - total_amount + 1

    discount_slices = []

    # 사야할 물건의 수량단위로 잘라서,
    # 일자별 dict 생성
    for i in range(last_start_no):
        product_count_map = {}
        for j in range(i, i + total_amount):
            product_count_map.setdefault(discount[j], 0)
            product_count_map[discount[j]] += 1
        discount_slices.append(product_count_map)

    # 할인 정보 슬라이스 dict 배열
    # print(discount_slices)

    # Python에서는 dict 자체가 통체로 비교가 된다고 해서... 비교 대상 맵을 만들자!,
    expect_slice = {}
    for i, want_slice in enumerate(want):
        expect_slice.setdefault(want_slice, number[i])

    answer = 0
    for i, discount_slice in enumerate(discount_slices):
        if discount_slice == expect_slice:
            # 💡 제품을 모두 할인 받을 수 있는 회원 등록 날짜의 총 일 수 임을 고려하자!
            answer += 1

    return answer


if __name__ == "__main__":
    print(
        solution(
            ["banana", "apple", "rice", "pork", "pot"],
            [3, 2, 2, 2, 1],
            [
                "chicken",
                "apple",
                "apple",
                "banana",
                "rice",
                "apple",
                "pork",
                "banana",
                "pork",
                "rice",
                "pot",
                "banana",
                "apple",
                "banana",
            ],
        )
    )
    print(
        solution(
            ["apple"],
            [10],
            [
                "banana",
                "banana",
                "banana",
                "banana",
                "banana",
                "banana",
                "banana",
                "banana",
                "banana",
                "banana",
            ],
        )
    )


### 검토 ###
# 일단 풀기는 풀었는데... Python이라서 뭔가 dict 다루기가 쉬워보인다.👍
# 다른 언어로는 어떻게 풀까? 😅
#
# 처음에 12번만 테스트케이스가 통과해서, 뭔가 했는데, 문제를 제대로 안읽었나보다. 😂
# 모두 살 수있는 시작 일자가 아니고,
# 제품을 모두 할인 받을 수 있는 회원 등록 날짜의 총 일수 이다. 😂😂
# +1로 통과 했음.
#
