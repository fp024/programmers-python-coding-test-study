################################################################################
# [연습문제 000_001] 트리의 순회
#
# 배열기반의 완전 이진트리에 대해서, 전위/중위/후위 순회 결과를 문자열로 출력
#
################################################################################

from dataclasses import dataclass


def pre_order_str(nodes: list[int]) -> str:
    """전위 순회 결과를 문자열로 반환"""
    root_idx = 0
    stack = [root_idx]
    result = ""
    node_length = len(nodes)

    while len(stack) > 0:
        # P: 부모에 먼저 방문
        current_node_idx = stack.pop()
        result += str(nodes[current_node_idx]) + " "

        right_child_idx = current_node_idx * 2 + 2
        left_child_idx = current_node_idx * 2 + 1
        # R: 스택이 LIFO이므로 R을 먼저 넣는다.
        if right_child_idx < node_length:
            stack.append(right_child_idx)
        # L: 스택이 LIFO이므로 L을 나중에 넣는다.
        if left_child_idx < node_length:
            stack.append(left_child_idx)

    return result[:-1]


@dataclass(frozen=True)  # 항상 새로 만들어서 사용하므로 불변으로 설정해도 된다.
class StackFrame:
    """스택 프레임 정보"""

    node_idx: int  # 노드 인덱스
    visited: bool  # 방문 여부


def in_order_str(nodes: list[int]) -> str:
    """중위 순회 결과를 문자열로 반환"""
    root_idx = 0
    stack = [StackFrame(root_idx, False)]
    result = ""
    node_length = len(nodes)

    while len(stack) > 0:
        current_node = stack.pop()

        if current_node.visited:
            result += str(nodes[current_node.node_idx]) + " "
        else:
            # R:
            right_child_idx = current_node.node_idx * 2 + 2
            if right_child_idx < node_length:
                stack.append(StackFrame(right_child_idx, False))
            # P:
            stack.append(StackFrame(current_node.node_idx, True))

            # L:
            left_child_idx = current_node.node_idx * 2 + 1
            if left_child_idx < node_length:
                stack.append(StackFrame(left_child_idx, False))

    return result[:-1]


def post_order_str(nodes: list[int]) -> str:
    """후위 순회 결과를 문자열로 반환"""

    root_idx = 0
    stack = [StackFrame(root_idx, False)]
    result = ""
    node_length = len(nodes)

    while len(stack) > 0:
        current_node = stack.pop()

        if current_node.visited:
            result += str(nodes[current_node.node_idx]) + " "
        else:
            # P:
            stack.append(StackFrame(current_node.node_idx, True))

            # R:
            right_child_idx = current_node.node_idx * 2 + 2
            if right_child_idx < node_length:
                stack.append(StackFrame(right_child_idx, False))

            # L:
            left_child_idx = current_node.node_idx * 2 + 1
            if left_child_idx < node_length:
                stack.append(StackFrame(left_child_idx, False))

    return result[:-1]


def solution(nodes: list[int]) -> list[str]:
    return [pre_order_str(nodes), in_order_str(nodes), post_order_str(nodes)]


if __name__ == "__main__":
    print(solution([1, 2, 3, 4, 5, 6, 7]))

### 검토 ###
#
# 💡 입력값이 배열로 표현된 이진트리이므로 트리로 만들 필요는 없다
#     순회만 제대로 하면 된다.
#
#  반복으로 순회 구현 부분이 잘 생각이 안나서,
#  먼저 C#으로 진행했던 아래 코드를 참고해서 바꿔보았다.
#  * https://github.com/fp024/programmers-csharp-coding-test-study/blob/master/Programmers.Solutions.Modern/Lv03/Exam42892A.cs
#
