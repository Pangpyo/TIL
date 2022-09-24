# 2022 카카오 양과 늑대



def dfs(n, s, w, pos) :
    print(n, s, w, pos)
    global graph
    global sheeps
    sheeps = s if s > sheeps else sheeps
    if s <= w :
        return
    pos.remove(n)
    for i in pos :
        print(i, pos)
        if not info[i] :
            dfs(i, s+1, w, pos+graph[i])
        else :
            dfs(i, s, w+1, pos+graph[i])


def solution(info, edges):
    global graph
    global sheeps
    N = len(info)
    graph = [[] for _ in range(N)]
    for u, v in edges :
        graph[u].append(v)
    print(graph)
    sheeps = 0
    pos = [0]
    dfs(0, 1, 0, pos+graph[0])
    return sheeps

info = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]

print(solution(info, edges))