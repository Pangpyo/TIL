# 코드몬스터 4

from collections import deque


def solution(edges, roots):
    n = len(edges) + 1
    que = deque()
    for i, edge in enumerate(edges):
        que.append([i, list(edge)])
    answer = [0] * n
    for root in roots:
        parent = deque([root])
        i = 0
        nque = deque()
        quel = len(que)
        while que:
            edge = que.popleft()
            if parent[0] in edge[1]:
                if edge[1][0] != parent[0]:
                    edge[1] = edge[1][::-1]
                    answer[edge[0]] += 1
                nque.append(edge)
                parent.append(edge[1][1])
            else:
                que.append(edge)
            i += 1
            if i == quel:
                parent.popleft()
                i = 0
                quel = len(que)
        que = nque
    return answer


edges = [[1, 3], [1, 2], [2, 4], [2, 5]]
roots = [2, 3]

print(solution(edges, roots))
