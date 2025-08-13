##################################################################################
# 기능 개발 - 42586
#   - https://school.programmers.co.kr/learn/courses/30/lessons/42586
#
##################################################################################
from math import ceil
from collections import deque


def solution(progresses: list[int], speeds: list[int]) -> list[int]:

    deploy_queue = deque(ceil((100 - p) / s) for p, s in zip(progresses, speeds))

    answer = [1]
    base_deploy = deploy_queue.popleft()

    while deploy_queue:
        next_task_deploy_day = deploy_queue.popleft()
        if base_deploy >= next_task_deploy_day:
            answer[-1] += 1
        else:
            base_deploy = next_task_deploy_day
            answer.append(1)

    return answer


if __name__ == "__main__":
    print(solution([93, 30, 55], [1, 30, 5]))
    print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))


### 검토 ###
# 일단 풀기는 풀었음..😅
# 1. 각 테스크 별 예상 배포일을 먼저 구해서 큐에다 넣어둠
# 2. 큐에서 값을 빼내면서, 다음 작업이 같거나 작으면 현재 배포묶음에 포함시켜서 1증가
#   - 다음작업이 더 크면 기준을 다음 배포 작업일 기준으로 바꾸고 새로 배포묶음 1로 추가
#
