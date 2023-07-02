# 2310 어드벤처 게임 G4

from collections import deque
import sys


def solution() :
    input = sys.stdin.readline
    answer = []
    while True :
        n = int(input())
        if not n :
            break
        visit = [[0]*501 for _ in range(n+1)]
        door = [[] for _ in range(n+1)]
        room = ['']*(n+1)
        costs = [0]*(n+1)
        for i in range(1, n+1) :
            temp = list(input().split())
            room[i] = temp[0]
            costs[i] = int(temp[1])
            for j in map(int, temp[2:-1]) :
                door[i].append(j)
        que = deque([(1, 0)])
        visit[1][0] = 1
        ans = "No"
        while que :
            x, m = que.popleft()
            for nx in door[x] :
                nm = m
                t, c = room[nx], costs[nx]
                if t == "L" :
                    nm = max(nm, c)
                elif t == "T" :
                    nm -= c
                if nm < 0 :
                    continue
                if visit[nx][nm] :
                    continue
                if nx == n :
                    ans = "Yes"
                    break
                que.append((nx, nm))
                visit[nx][nm] = 1
        answer.append(ans)
    return answer

if __name__ == "__main__" :
    print(*solution(), sep="\n")