################################################################################
# 카드 뭉치 - 159994
#   - https://school.programmers.co.kr/learn/courses/30/lessons/159994
#
################################################################################
from collections import deque


def solution(cards1: list[str], cards2: list[str], goal: list[str]) -> str:
    goal_queue = deque(goal)
    cards1_queue = deque(cards1)
    cards2_queue = deque(cards2)

    while goal_queue:
        target = goal_queue[0]
        if cards1_queue and cards1_queue[0] == target:
            cards1_queue.popleft()
            goal_queue.popleft()
        elif cards2_queue and cards2_queue[0] == target:
            cards2_queue.popleft()
            goal_queue.popleft()
        else:
            break

    # 💡 3항연산: 참일때값 if 조건 else 거짓일때값
    #     queue가 비엇을때가 거짓으로 판단하므로 다음과 같이 구현한다.
    return "No" if goal_queue else "Yes"


if __name__ == "__main__":
    print(
        solution(
            ["i", "drink", "water"],
            ["want", "to"],
            ["i", "want", "to", "drink", "water"],
        )
    )
    print(
        solution(
            ["i", "water", "drink"],
            ["want", "to"],
            ["i", "want", "to", "drink", "water"],
        )
    )


### 검토 ###
# - 3항 연산자가 특이하다. C, Java와는 다름 😅
# - 이제부터 테스트 케이스 데이터에 namedtuple을 사용했는데, 꽤 괜찮다. 👍
#
