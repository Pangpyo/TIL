# 20947 습격받은 도시 G4

import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    city = tuple(list(input().rstrip()) for _ in range(N))
    check = [[0]*N for _ in range(N)]
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    for x in range(N):
        for y in range(N):
            if city[x][y] == 'O':
                for i in range(4):
                    nx = x
                    ny = y
                    while True :
                        nx += dx[i]
                        ny += dy[i]
                        if nx >= N or nx < 0 or ny >= N or ny < 0:
                            break
                        if city[nx][ny] != '.':
                            break
                        check[nx][ny] = 1
    answer = []
    for i in range(N):
        for j in range(N):
            if city[i][j] == '.' and not check[i][j]:
                city[i][j] = 'B'
        answer.append(''.join(city[i]))
    return answer

if __name__ == "__main__":
    print(*solution(), sep='\n')