################################################################################
# 두 개 뽑아서 더하기 - 68644
#   - https://school.programmers.co.kr/learn/courses/30/lessons/68644
#
################################################################################
def solution(arr: list[int]):
    size = len(arr)
    unique_set = set()

    for i in range(size):
        for j in range(i + 1, size):
            unique_set.add(arr[i] + arr[j])

    result = list(unique_set)
    result.sort()
    return result


if __name__ == "__main__":
    print(solution([2, 1, 3, 4, 1]))
    print(solution([5, 0, 2, 7]))
