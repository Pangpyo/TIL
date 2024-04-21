# 20165 인내의 도미노 장인 호석 G5

import sys


def solution():
    input = sys.stdin.readline
    N, M, R = map(int, input().split())
    domino = tuple(tuple(map(int, input().split())) for _ in range(N))
    dr = {'N':0, 'E':1, 'S':2, 'W':3}
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    visit = [['S']*M for _ in range(N)]
    answer = 0
    def attack(x, y, d):
        if visit[x][y] == 'F':
            return 0
        visit[x][y] = 'F'
        score = 1
        for i in range(1, domino[x][y]):
            nx = x + dx[d]*i
            ny = y + dy[d]*i
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            score += attack(nx, ny, d)
        return score
    def deffence(x, y):
        visit[x][y] = 'S'
    for _ in range(R):
        x, y, d = input().split()
        answer += attack(int(x)-1, int(y)-1, dr[d])
        x, y = map(int, input().split())
        deffence(x-1, y-1)
    print(answer)
    for v in visit:
        print(*v)

if __name__ == "__main__":
    solution()
