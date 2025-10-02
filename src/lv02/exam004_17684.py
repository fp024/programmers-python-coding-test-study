##################################################################################
# 압축 - 17684
#   - https://school.programmers.co.kr/learn/courses/30/lessons/17684
#
##################################################################################


# 사전 초기화
def init_dict() -> dict[str, int]:
    word_dict = {}
    for i in range(26):
        word_dict[chr(ord("A") + i)] = i + 1
    return word_dict


def solution(msg: str) -> list[int]:
    word_dict = init_dict()
    answer = []

    # for-range 반복 내에서 i를 수정하기 힘드므로, while을 쓰는게 낫다.
    i = 0
    while i < len(msg):
        # 사전에서 찾은 가장 긴 단어
        found_long_word = ""

        for j in range(i, len(msg)):
            next_char = msg[j]

            if found_long_word + next_char in word_dict:
                found_long_word += next_char
            else:
                word_dict[found_long_word + next_char] = len(word_dict) + 1
                break

        i += len(found_long_word)
        answer.append(word_dict[found_long_word])

    return answer


# cspell:disable
if __name__ == "__main__":
    print(solution("KAKAO"))

    print(solution("TOBEORNOTTOBEORTOBEORNOT"))

    print(solution("ABABABABABABABAB"))

### 검토 ###
# 뭔가 어렵다..😂고 느껴서, Java로는 먼저 풀었다.
# * Java 풀이
#   https://github.com/fp024/programmers-java-coding-test-study/blob/master/src/test/java/org/fp024/lv02/Exam17684Tests.java
#
# Java로 먼저 풀은 로직 그대로 풀어봤다. 😅
#
