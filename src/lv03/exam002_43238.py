################################################################################
# 입국심사 - 43238
#   - https://school.programmers.co.kr/learn/courses/30/lessons/43238
#
################################################################################


def solution(n: int, times: list[int]) -> int:
    left = min(times)  # 1명을 처리할 수 있는 최소 시간으로 초기값 설정
    right = n * max(times)  # 모든 사람을 처리할 수 있는 최대 시간으로 초기값 설정
    answer = right  # 최대 값으로 초기화 (안전장치)

    while left <= right:
        mid = (left + right) // 2  # 중간 시간 값 계산
        # mid 시간 내에 심사 가능한 인원 계산
        count = sum(mid // time for time in times)

        if count < n:  # 시간이 부족함, 더 긴 시간 필요
            left = mid + 1
        else:  # 시간이 충분함, 더 짧은 시간 시도
            answer = mid  # 💡 "이 시간이면 n명 이상 처리 가능", → 조건 만족! 더 짧은 시간도 시도해보자!
            right = mid - 1

    return answer


# cspell:disable
if __name__ == "__main__":
    print(solution(6, [7, 10]))
# cspell:enable


### 검토 ###
# AI에게 힌트를 엄청 물어보고 답은 나왔는데, 뭔가 자력이 아니라서 😂
#
