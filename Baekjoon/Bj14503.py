# 15503 로봇청소기 G5

N, M = map(int, input().split())

r, c, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = 0

visit = [[0] * M for _ in range(N)]


def clean(r, c):
    global ans
    visit[r][c] = 1
    ans += 1
    search(r, c)


def look(d, n):
    see = d - n
    if see == -1:
        see = 3
    return see


def search(r, c):
    global d
    for _ in range(4):
        d = look(d, 1)
        # print(r, c, d)
        nr = r + dx[d]
        nc = c + dy[d]
        if nr >= N or nr < 0 or nc >= M or nc < 0:
            continue
        if room[nr][nc] or visit[nr][nc]:
            continue
        clean(nr, nc)
        return
    back = look(d, 2)
    br = r + dx[back]
    bc = c + dy[back]
    if br >= N or br < 0 or bc >= M or bc < 0 or room[br][bc]:
        return
    search(br, bc)


clean(r, c)

print(ans)
