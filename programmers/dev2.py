from collections import deque


def solution(maps):
    N = len(maps)
    M = len(maps[0])
    for i in range(len(maps)):
        maps[i] = list(maps[i])

    visit = [[0] * M for _ in range(N)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    members = {}

    def bfs(x, y):
        que = deque([(x, y)])
        dic = {}
        visit[x][y] = 1
        while que:
            x, y = que.popleft()
            if maps[x][y] not in dic:
                dic[maps[x][y]] = 1
            else:
                dic[maps[x][y]] += 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= N or nx < 0 or ny >= M or ny < 0:
                    continue
                if maps[nx][ny] == "." or visit[nx][ny] == 1:
                    continue
                visit[nx][ny] = 1
                que.append((nx, ny))
        return dic

    for i in range(N):
        for j in range(M):
            if maps[i][j] == "." or visit[i][j] == 1:
                continue
            dic = bfs(i, j)
            if not dic:
                continue
            item = sorted(dic.items(), key=lambda x: (x[1], x[0]), reverse=True)
            winner, winland = item[0]
            for loser, land in item:
                if land == winland:
                    continue
                dic[loser] = 0
                dic[winner] += land
            for k, v in dic.items():
                if k not in members:
                    members[k] = v
                else:
                    members[k] += v
    print(members)
    answer = sorted(members.items(), key=lambda x: -x[1])[0][1]
    return answer


maps = [
    "AABCA.QA",
    "AABC..QX",
    "BBBC.Y..",
    ".A...T.A",
    "....EE..",
    ".M.XXEXQ",
    "KL.TBBBQ",
]

print(solution(maps))
