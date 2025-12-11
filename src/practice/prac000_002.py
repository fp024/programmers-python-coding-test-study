################################################################################
# [연습문제 000_002] 이진 탐색 트리 구현
#
# 이진 탐색 트리 구현 후, 검색 값 조회 결과 반환
#
################################################################################

from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    """이진 탐색 트리 노드 클래스"""

    value: int  # 노드에 저장된 값
    left: Optional["Node"] = None  # 왼쪽 자식 노드
    right: Optional["Node"] = None  # 오른쪽 자식 노드


# python:S3516 항상 같은 값을 반환한다고, SonarQube가 오탐지. 😆
# 그외 복잡도가 높아서 발생한 python:S3776는 여기선 무시하자...😅
def make_bst(lst: list[int]) -> Node:  # NOSONAR
    """BST 생성 함수"""

    if not lst:  # ← 추가
        raise ValueError("빈 리스트로는 BST를 생성할 수 없습니다")

    root = Node(value=lst[0])
    if len(lst) == 1:
        return root

    for i in range(1, len(lst)):
        current_root = root
        new_node = Node(value=lst[i])

        while True:
            if new_node.value < current_root.value:
                if current_root.left is None:
                    current_root.left = new_node
                    break
                else:
                    current_root = current_root.left
            elif new_node.value > current_root.value:
                if current_root.right is None:
                    current_root.right = new_node
                    break
                else:
                    current_root = current_root.right
            else:
                raise ValueError(
                    f"중복된 값 {new_node.value}는 이진 탐색 트리에 추가할 수 없습니다"
                )

    return root


def is_exist(s: int, root: Node) -> bool:
    """값이 BST에 존재하는지 확인하는 함수"""

    current_node: Optional["Node"] = root

    while current_node is not None:
        if s == current_node.value:
            return True
        elif s > current_node.value:
            current_node = current_node.right
        else:
            current_node = current_node.left

    return False


def solution(lst: list[int], search_lst: list[int]) -> list[bool]:
    root = make_bst(lst)  # 이진 탐색 트리의 루트 노드

    return [is_exist(s, root) for s in search_lst]


if __name__ == "__main__":
    print(solution([1], [1]))
    print(solution([1, 2, 3], [1, 2, 3]))
    print(solution([5, 3, 8, 4, 2, 1, 7, 10], [1, 2, 5, 6]))
    print(solution([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))


### 검토 ###
#
# 자력으로 풀긴하는데... 너무 오래걸린다. 😂
#
