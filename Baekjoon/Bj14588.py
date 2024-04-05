# 14588 Line Friends (Small) G5

import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    lines = tuple(tuple(map(int, input().split())) for _ in range(N))
    Q = int(input())
    answers = [-1]*Q
    INF = 600
    dist = [[INF if i != j else 0 for j in range(N)] for i in range(N)]
    for i in range(N):
        s, e = lines[i]
        for j in range(i+1, N):
            ns, ne = lines[j]
            if s <= ns <= e or s <= ne <= e or ns <= s <= ne or ns <= e <= ne:
                dist[i][j] = 1
                dist[j][i] = 1
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    for q in range(Q):
        a, b = map(lambda x : int(x)-1, input().split())
        if dist[a][b] != INF :
            answers[q] = dist[a][b]

    return answers

if __name__ == "__main__":
    print(*solution(), sep='\n')