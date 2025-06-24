def solution(num1, num2):
    if not (isinstance(num1, int) and isinstance(num2, int)):
        raise TypeError("입력값은 정수여야 합니다.")
    answer = num1 + num2
    return answer
