# 1197 최소 스패닝 트리 G4

import sys


input = sys.stdin.readline

V, E = map(int, input().split())

parent = [i for i in range(0, V + 1)]

graph = []


def find(x):
    if x == parent[x]:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[max(x, y)] = min(x, y)
        return True
    else:
        return False


# 유니온 파인드 함수 구현

for i in range(E):
    graph.append(tuple(map(int, input().split())))

graph.sort(key=lambda x: x[2])  # 간선들을 크기가 작은 순으로 하나씩 검사한다.
ans = 0
for u, v, l in graph:
    if union(u, v):  # 유니온 파인드를 할 때 x와 y가 사이클이 되지 않을 경우에만 간선의 길이를 더해준다.
        ans += l
print(ans)
