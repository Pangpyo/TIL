# 30024 옥수수밭 G4

from heapq import heappop, heappush
import sys


def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    corns = [list(map(int, input().split())) for _ in range(N)]
    heap = []
    visit = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if i == 0 or j == 0 or i == N-1 or j == M-1:
                visit[i][j] = 1
                heappush(heap, (-corns[i][j], i, j))
    K = int(input())
    print(*visit, sep='\n')
    answer = []
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    for i in range(K):
        c, x, y = heappop(heap)
        answer.append(' '.join(map(str, (x+1, y+1))))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visit[nx][ny]:
                continue
            heappush(heap, (-corns[nx][ny], nx, ny))
            visit[nx][ny] = 1
    return answer

if __name__ == "__main__":
    print(*solution(), sep='\n')