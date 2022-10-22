# 1068 트리 G5

N = int(input())

nodes = list(map(int, input().split()))
delnode = int(input())
graph = [[] for _ in range(N)]

for i in range(N):  # 시작노드를 설정하고, 단방향 그래프를 만들어준다.
    if nodes[i] == -1:
        start = i
    else:
        graph[nodes[i]].append(i)
ans = 0


def dfs(n):  # 그래프를 순회하며 del노드가 아닌경우 끝까지 가준다.
    global ans
    point = True
    if graph[n]:
        for nn in graph[n]:  # 자식 노드를 순회한다.
            if nn != delnode:
                dfs(nn)
                point = False  # 자식노드가 하나라도 있을 경우 point를 False로 만들어준다.

    if point:  # point가 True인 경우, 즉 자식노드가 하나도 없는 리프노드일 경우 ans += 1
        ans += 1


if start != delnode:  # start와 delnode가 같을 경우 함수를 실행하지 않고, 답은 0이 된다.
    dfs(start)

print(ans)
