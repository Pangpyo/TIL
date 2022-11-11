# 2623 음악프로그램 G3

from collections import deque
import sys

# input = sys.stdin.readline

sys.stdin = open("input.txt")

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
lines = [0] * (N + 1)
for i in range(M):
    nums = list(map(int, input().split()))
    for j in range(1, nums[0] + 1):
        if j > 1:
            lines[nums[j]] += 1
        if j < nums[0]:
            graph[nums[j]].append(nums[j + 1])

visit = [0] * (N + 1)
finished = [0] * (N + 1)

cycle = False


def bfs(n):
    global cycle
    visit[n] = 1
    for nn in graph[n]:
        if not visit[nn]:
            bfs(nn)
        else:
            if not finished[nn]:
                cycle = 1
    finished[n] = 1


for i in range(1, N + 1):
    if cycle:
        break
    if not visit[i]:
        bfs(i)

if not cycle:
    que = deque()
    for i in range(1, N + 1):
        if lines[i] == 0:
            que.append(i)

    while que:
        n = que.popleft()
        print(n)
        for nn in graph[n]:
            lines[nn] -= 1
            if lines[nn] == 0:
                que.append(nn)
else:
    print(0)
