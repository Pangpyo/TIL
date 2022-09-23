# 1991 트리 순회 S1

N = int(input())
graph = [[0, 0, 0] for _ in range(N+1)]
for i in range(1, N+1) :
    root, left, right = map(ord, input().split())
    root -= 64
    left = 0 if left == 46 else left-64
    right = 0 if right == 46 else right-64
    graph[root][1] = left
    graph[root][2] = right
    if left :
        graph[left][0] = root
    if right :
        graph[right][0] = root

def pre(n) :
    print(chr(n+64), end='')
    if graph[n][1] :
        pre(graph[n][1])
    if graph[n][2] :
        pre(graph[n][2])


def mid(n) :
    if graph[n][1] :
        mid(graph[n][1])
    print(chr(n+64), end='')
    if graph[n][2] :
        mid(graph[n][2])
    
def post(n) :
    if graph[n][1] :
        post(graph[n][1])
    if graph[n][2] :
        post(graph[n][2])
    print(chr(n+64), end='')
pre(1)
print()
mid(1)
print()
post(1)
