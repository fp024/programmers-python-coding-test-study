################################################################################
# 완주하지 못한 선수 - 42576
#   - https://school.programmers.co.kr/learn/courses/30/lessons/42576
#
################################################################################


def solution(participant: list[str], completion: list[str]) -> str:

    participant_map = {}
    answer = ""

    # <참여자 선수이름, 참여자수(동명이인 체크)>로 맵을 구성
    for player in participant:
        participant_map.setdefault(player, 0)
        participant_map[player] += 1

    # 완료자 목록 기준으로 참여자 수 빼주기
    for finish_player in completion:
        participant_map[finish_player] -= 1

    # 동명이인의 이름은 여러명이 있을 수 있지만,
    # 완주하지 못한 사람의 이름은 1명임 😅
    # 문제 구조상 participant_map을 구성할 때...
    # 이미 완주자 목록 검사할 필요없이,
    # 동명이인이 발견되면.. 그게 답이 될 수 있을 것 같다. 😅
    # 그래도... 동명이인이 없는 경우는 completion를 참고하긴해야함. 😅
    for player in participant_map:
        if participant_map[player] > 0:
            answer = player
            break

    return answer


# cspell:disable
if __name__ == "__main__":
    print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
    print(
        solution(
            ["marina", "josipa", "nikola", "vinko", "filipa"],
            ["josipa", "filipa", "marina", "nikola"],
        )
    )
    print(
        solution(
            ["mislav", "stanko", "mislav", "ana"],
            ["stanko", "ana", "mislav"],
        )
    )

### 검토 ###
# ...
#
