# 17144 미세먼지 안녕! G4


r, c, t = map(int, input().split())

room = []
cleaner = 0
for i in range(r):
    line = list(map(int, input().split()))
    if not cleaner:
        if -1 in line:
            cleaner = (i, line.index(-1))
    room.append(line)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def spread():  # 미세먼지 확산부분 구현
    global r, c
    nextroom = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            cnt = 0
            if room[x][y] < 0:  # 공기청정기 칸일경우 컨티뉴
                continue
            dust = room[x][y] // 5
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= r or nx < 0 or ny >= c or ny < 0:
                    continue
                if (nx, ny) == cleaner or (nx, ny) == (
                    cleaner[0] + 1,
                    cleaner[1],
                ):  # 공기청정기 칸일경우 컨티뉴
                    continue
                nextroom[nx][ny] += dust
                cnt += 1
            nextroom[x][y] += room[x][y] - dust * cnt
    nextroom[cleaner[0]][cleaner[1]] = -1
    nextroom[cleaner[0] + 1][cleaner[1]] = -1
    return nextroom


def circulate():  # 순환부분 구현
    global r, c
    pre = 0
    d = 0
    x1 = cleaner[0]
    y1 = cleaner[1]
    while 1:  # 공기청정기 상단부분
        if d == 0:
            if y1 + 1 < c:
                y1 += 1
            else:
                d = 1
                continue
        elif d == 1:
            if x1 - 1 >= 0:
                x1 -= 1
            else:
                d = 2
                continue
        elif d == 2:
            if y1 - 1 >= 0:
                y1 -= 1
            else:
                d = 3
                continue
        else:
            if x1 + 1 <= cleaner[0]:
                x1 += 1
            else:
                d = 0
                continue
        if (x1, y1) == cleaner:
            break
        room[x1][y1], pre = pre, room[x1][y1]
    pre = 0
    d = 0
    x2 = cleaner[0] + 1
    y2 = cleaner[1]
    while 1:  # 공기청정기 하단부분
        if d == 0:
            if y2 + 1 < c:
                y2 += 1
            else:
                d = 1
                continue
        elif d == 1:
            if x2 + 1 < r:
                x2 += 1
            else:
                d = 2
                continue
        elif d == 2:
            if y2 - 1 >= 0:
                y2 -= 1
            else:
                d = 3
                continue
        else:
            if x2 - 1 >= cleaner[0] + 1:
                x2 -= 1
            else:
                d = 0
                continue
        if (x2, y2) == (cleaner[0] + 1, cleaner[1]):
            break
        room[x2][y2], pre = pre, room[x2][y2]


for i in range(t):
    room = spread()
    circulate()
print(sum(map(sum, room)) + 2)
