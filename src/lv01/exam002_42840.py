################################################################################
# 모의고사 - 42840
#   - https://school.programmers.co.kr/learn/courses/30/lessons/42840
#
#   - 💡프로그래머스에 제출할 때는 함수 정의의 힌트를 제거해야한다.
################################################################################
def solution(answers: list[int]) -> list[int]:
    user_patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
    ]

    scores = [0] * len(user_patterns)

    for i, answer in enumerate(answers):
        for u, user_pattern in enumerate(user_patterns):
            if answer == user_pattern[i % len(user_pattern)]:
                scores[u] += 1

    max_score = max(scores)

    result: list[int] = []

    for i, s in enumerate(scores):
        if max_score == s:
            result.append(i + 1)

    return result


if __name__ == "__main__":
    print(solution([1, 2, 3, 4, 5]))
    print(solution([1, 3, 2, 4, 2]))
    print(solution([5, 1, 1]))
