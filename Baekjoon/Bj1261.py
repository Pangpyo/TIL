# 1261 알고스팟 G4
# from heapq import heappop, heappush


# M, N = map(int, input().split())

# miro = [list(input()) for _ in range(N)]


# def dijkstra():  # 벽이 없는 경우 거리가 0, 있는 경우 거리가 1인것으로 생각하고 다익스트라를 쓰자!(BFS사용시 시간초과)
#     que = []
#     que.append((0, 0, 0))  # 거리, x, y
#     dx = [-1, 0, 1, 0]
#     dy = [0, 1, 0, -1]
#     inf = 201
#     D = [[inf] * M for _ in range(N)]
#     D[0][0] = 0
#     while que:
#         d, x, y = heappop(que)
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx >= N or nx < 0 or ny >= M or ny < 0:
#                 continue
#             if D[nx][ny] == inf:
#                 # 다익스트라는 heap을 사용해 그리디하게 거리를 가져오고, 모든 정점의 거리는 1또는 0이므로
#                 # 한번이라도 방문했다면 그것이 최소값.
#                 # D[nx][ny] > d+1 이렇게 했다가 괜히 탐색수가 많아져서 시간초과 났었음.
#                 if miro[nx][ny] == "1":
#                     D[nx][ny] = d + 1
#                     heappush(que, (d + 1, nx, ny))
#                 else:
#                     D[nx][ny] = d
#                     heappush(que, (d, nx, ny))
#     return D[-1][-1]


# print(dijkstra())

from collections import deque

M, N = map(int, input().split())

miro = [list(input()) for _ in range(N)]


def bfs():  # 0-1 bfs 사용시
    que = deque()
    que.append((0, 0))  # 거리, x, y
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    inf = 201
    D = [[inf] * M for _ in range(N)]
    D[0][0] = 0
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            if D[nx][ny] == inf:  # 가고자 하는 정점이 방문하지 않은 정점인 경우
                if miro[nx][ny] == "1":  # 벽이 있을 경우
                    D[nx][ny] = D[x][y] + 1  # 현재까지 부순 벽의 개수 + 1
                    que.append((nx, ny))  # 큐의 뒤로 append
                else:
                    D[nx][ny] = D[x][y]  # 벽이 없을 경우는 그대로
                    que.appendleft((nx, ny))  # 거리가 더 가까운 경우이므로 큐의 앞으로 append
    return D[-1][-1]


print(bfs())
