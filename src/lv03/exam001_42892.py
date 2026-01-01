################################################################################
# 길 찾기 게임 - 42892
#   - https://school.programmers.co.kr/learn/courses/30/lessons/42892
#
################################################################################
from dataclasses import dataclass
from typing import NamedTuple


@dataclass
class Node:
    """
    노드 클래스
    """

    id: int
    x: int
    y: int
    left: "Node" = None
    right: "Node" = None


def insert_node(root, new_node):
    """
    노드 삽입
    """
    parent_node = root

    while True:
        if parent_node.x > new_node.x:
            if parent_node.left is None:
                parent_node.left = new_node
                break

            parent_node = parent_node.left

        elif parent_node.x < new_node.x:
            if parent_node.right is None:
                parent_node.right = new_node
                break
            parent_node = parent_node.right
        else:
            raise ValueError(
                f"노드의 x 좌표가 중복되었습니다.  부모 노드: {parent_node}, 신규 노드: {new_node}"
            )


def construct_tree(nodeinfo: list[list[int]]) -> Node:
    """
    이진 트리 생성
    :param nodeinfo: 노드 정보
    :return: 생성된 트리의 루트 노드
    """

    # Node를 생성하면서, y축 기준으로 정렬
    nodes = [Node(idx + 1, raw[0], raw[1]) for idx, raw in enumerate(nodeinfo)]
    nodes.sort(key=lambda n: n.y, reverse=True)

    # root노드는 y축 값이 가장 큰 좌표의 노드
    root = nodes[0]

    # 노드 삽입 (루트 노드를 제외한 노드 삽입 반복)
    for new_node in nodes[1:]:
        insert_node(root, new_node)

    return root


def pre_order(root: Node) -> list[int]:
    """
    전위 순회  P -> L -> R
    :param root: 루트 노드
    :return: 전위 순회 방문 결과
    """
    visits = []
    stack = [root]

    while stack:
        current_node = stack.pop()
        visits.append(current_node.id)

        if current_node.right is not None:
            stack.append(current_node.right)

        if current_node.left is not None:
            stack.append(current_node.left)

    return visits


def post_order(root: Node) -> list[int]:
    """
    후위 순회 L -> R -> P
    :param root: 루트 노드
    :return: 후위 순회 방문 결과
    """

    class StackFrame(NamedTuple):
        """
        후위순회 상태 저장을 위한 스택 프레임
        """

        node: Node
        visited: bool

    stack: list[StackFrame] = [StackFrame(root, False)]
    visits: list[int] = []

    while stack:
        current_node, visited = stack.pop()

        if visited:
            visits.append(current_node.id)
        else:
            stack.append(StackFrame(current_node, True))

            if current_node.right is not None:
                stack.append(StackFrame(current_node.right, False))

            if current_node.left is not None:
                stack.append(StackFrame(current_node.left, False))

    return visits


def solution(nodeinfo: list[list[int]]) -> list[list[int]]:

    root = construct_tree(nodeinfo)

    pre_order_result = pre_order(root)
    post_order_result = post_order(root)

    return [pre_order_result, post_order_result]


# cspell:disable
if __name__ == "__main__":
    print(
        solution(
            [
                [5, 3],  #
                [11, 5],
                [13, 3],
                [3, 5],
                [6, 1],
                [1, 3],
                [8, 6],
                [7, 2],
                [2, 2],
            ]
        )
    )
# cspell:enable


### 검토 ###
# 예전에 진행했던 C# 풀이코드를 바꿔봤다. 😅
#   https://github.com/fp024/programmers-csharp-coding-test-study/blob/master/Programmers.Solutions.Modern/Lv03/Exam42892A.cs
