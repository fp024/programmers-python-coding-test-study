################################################################################
# [연습문제 000_003] 다단계 칫솔 문제 변형 문제
#   [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/77486
#     위의 문제의 변형
#
################################################################################


def solution(
    enroll: list[str],
    referral: list[str],
    seller: list[str],
    amount: list[int],
    rates: list[int],
    unit_price: int,
    min_forward: int,
) -> list[int]:
    """
    다단계 칫솔 판매 문제 해결 함수

    :param enroll: 판매원 이름(조직 등록 순서)
    :param referral: 각 판매원의 추천인 이름, 센터는 "-"
    :param seller: 판매 발생 판매원 이름 목록
    :param amount: 각 판매 건의 판매 수량
    :param rates: 각 판매원의 상위로 전달하는 수수료율(%)
    :param unit_price: 상품 1개 가격
    :param min_forward: 상위로 전달할 최소 금액
    :return: 각 판매원이 얻은 이익금을 나열한 배열
    """
    # (1) parent 포인터: 자식 -> 부모(추천인)
    parent = dict(zip(enroll, referral))

    # (2) 수익 누적 맵: 판매원 -> 누적 이익
    profit = dict.fromkeys(enroll, 0)

    # (3) 수수료율 맵: 판매원 -> rate(%)
    enroll_rates = dict(zip(enroll, rates))

    for name, cnt in zip(seller, amount):
        money = cnt * unit_price
        cur = name

        while money > 0 and cur != "-":
            rate = enroll_rates[cur]  # 퍼센트

            if rate == 0:
                profit[cur] += money
                break

            forward = (money * rate) // 100  # 위로 보낼 돈
            keep = money - forward  # 내가 가질 돈

            if forward < min_forward:
                profit[cur] += money
                break

            profit[cur] += keep
            money = forward
            cur = parent[cur]

    return [profit[e] for e in enroll]


# cspell:disable
if __name__ == "__main__":
    print(
        solution(
            ["a", "b", "c", "d"],
            ["-", "a", "b", "b"],
            ["d", "d", "c"],
            [1, 2, 3],
            [0, 20, 30, 40],
            100,
            5,
        )
    )
# cspell:enable

### 검토 ###
# ...
#
