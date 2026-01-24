################################################################################
# 섬 연결하기 - 42861
#   - https://school.programmers.co.kr/learn/courses/30/lessons/41861
#
################################################################################


def find(parents: list[int], node: int) -> int:
    if parents[node] == node:
        return node

    # 💡 경로 압축을 동시에 수행
    parents[node] = find(parents, parents[node])
    return parents[node]


def union(parents: list[int], ranks: list[int], a_node: int, b_node: int) -> bool:
    a_root = find(parents, a_node)
    b_root = find(parents, b_node)

    if a_root == b_root:
        return False

    if ranks[a_root] > ranks[b_root]:
        parents[b_root] = a_root
    elif ranks[a_root] < ranks[b_root]:
        parents[a_root] = b_root
    else:
        parents[b_root] = a_root
        ranks[a_root] += 1
    return True


def solution(n: int, costs: list[list[int]]) -> int:
    # 비용 기준으로 costs 정렬
    sorted_costs = sorted(costs, key=lambda x: x[2])
    print(sorted_costs)

    # 각 노드가 부모 노드가 되도록 초기화
    parents = list(range(n))

    # 랭크 초기화
    ranks = [0] * n

    edge_count = 0
    min_cost = 0

    for a_node, b_node, cost in sorted_costs:
        # x, y가 서로 다른 집합에 속하면 집합 합치기
        if union(parents, ranks, a_node, b_node):
            # 현재 간선의 비용을 최소 비용에 추가
            min_cost += cost
            # 포함된 간선의 개수 증가
            edge_count += 1
            # n-1개의 간선이 선택된 상태면 반복 종료
            if edge_count == n - 1:
                break

    return min_cost


# cspell:disable
if __name__ == "__main__":
    print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))

# cspell:enable

### 검토 ###
# 일단 푸는 방법은 알고는 있는데, 뭔가 외워져서 알고있는 느낌..😅
#
# 복기를 해보면...
# 1. 비용기준 오름차순 결과
#    [
#      [0, 1, 1],
#      [1, 3, 1],
#      [0, 2, 2],
#      [1, 2, 5],
#      [2, 3, 8]
#    ]
# 2. 반복1 실행 이후: 0, 1 노드
#     트리
#         0
#        /
#       1
#     랭크 :   0  1  2  3
#           [1, 0, 0, 0]
#     간선 수: 1
#     비용   : 1
#
#    반복2 실행 이후: 1, 3 노드
#     트리
#         0
#        / \
#       1   3
#     랭크 :   0  1  2  3
#            [1, 0, 0, 0]
#     간선 수: 2
#     비용   : 2
#
#    반복3 실행 이후: 0, 2 노드
#     트리
#           0
#        / \  \
#       1   3  2
#     랭크 :   0  1  2  3
#            [1, 0, 0, 0]
#     간선 수: 3
#     비용   : 4
#
#    반복4 실행 이후: 1, 2 노드
#     트리
#           0
#        / \  \
#       1   3  2
#     랭크 :   0  1  2  3
#            [1, 0, 0, 0]
#     1, 2의 루트가 0이라서 변경없음
#     간선 수: 3
#     비용   : 4
#
#    반복4 실행 이후: 2, 3 노드
#     트리
#           0
#        / \  \
#       1   3  2
#     랭크 :   0  1  2  3
#            [1, 0, 0, 0]
#     2, 3의 루트가 0이라서 변경없음
#     간선 수: 3
#     비용   : 4
#
# 결과는 4
