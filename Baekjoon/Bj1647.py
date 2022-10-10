# 1647 도시분할계획 G4

N, M = map(int, input().split())

parent = [i for i in range(N + 1)]


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


graph = []

for i in range(M):
    graph.append(tuple(map(int, input().split())))

graph.sort(key=lambda x: x[2])  # 간선들을 크기가 작은 순으로 하나씩 검사한다.
ans = []
two = False
for u, v, l in graph:
    if union(u, v):  # 유니온 파인드를 할 때 x와 y가 사이클이 되지 않을 경우에만 간선의 길이를 더해준다.
        ans.append(l)
print(sum(ans[0:-1]))  # 가장 비용이 많이 드는 길 하나를 제외한 나머지 길을 합한다.
