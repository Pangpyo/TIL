# 23290 마법사 상어와 복제 G1

from itertools import product
import sys

input = sys.stdin.readline

fdx = [0, -1, -1, -1, 0, 1, 1, 1]
fdy = [-1, -1, 0, 1, 1, 1, 0, -1]

sdx = [-1, 0, 1, 0]
sdy = [0, -1, 0, 1]


class Fish:
    __slots__ = ("x", "y", "d", "cnt")

    def __init__(self, x, y, d, cnt, flag):
        self.x = x
        self.y = y
        self.d = d
        self.cnt = cnt
        if flag:
            nsea[x][y][d] = self
        else:
            sea[x][y][d] = self

    def move(self):
        for i in range(8):
            nd = (self.d - i) % 8
            nx = self.x + fdx[nd]
            ny = self.y + fdy[nd]
            if nx >= 4 or nx < 0 or ny >= 4 or ny < 0:
                continue
            if (nx, ny) == shark:
                continue
            if smells[nx][ny]:
                continue
            self.nput(nx, ny, nd)
            return
        self.put()

    def nput(self, nx, ny, nd):
        if nsea[nx][ny][nd]:
            nsea[nx][ny][nd].plus(self.cnt)
        else:
            Fish(nx, ny, nd, self.cnt, True)

    def put(self):
        if nsea[self.x][self.y][self.d]:
            nsea[self.x][self.y][self.d].plus(self.cnt)
        else:
            Fish(self.x, self.y, self.d, self.cnt, True)

    def plus(self, cnt):
        self.cnt += cnt

    def __str__(self) -> str:
        return "x : {}, y : {}, cnt : {}, d : {}".format(
            self.x, self.y, self.cnt, self.d
        )


permu = list(product(range(4), repeat=3))


def shark_move(shark):
    x, y = shark
    ex, ey = x, y
    route = (0, 0, 0)
    mcnt = -1
    visit = set()
    for per in permu:
        cnt = 0
        flag = True
        nx, ny = x, y
        visit.clear()
        for d in per:
            nx = nx + sdx[d]
            ny = ny + sdy[d]
            if nx >= 4 or nx < 0 or ny >= 4 or ny < 0:
                flag = False
                break
            for i in range(8):
                if nsea[nx][ny][i] and (nx, ny) not in visit:
                    cnt += nsea[nx][ny][i].cnt
            visit.add((nx, ny))
        if flag and cnt > mcnt:
            route = per
            mcnt = cnt
    nx, ny = x, y
    for d in route:
        nx = nx + sdx[d]
        ny = ny + sdy[d]
        for i in range(8):
            if nsea[nx][ny][i]:
                nsea[nx][ny][i] = None
                smells[nx][ny] = 2
        ex, ey = nx, ny
    return (ex, ey)


M, S = map(int, input().split())

fishes: list[Fish] = []

sea: list[Fish] = [[[None] * 8 for _ in range(4)] for _ in range(4)]
smells = [[0] * 4 for _ in range(4)]

for i in range(M):
    x, y, d = map(int, input().split())
    if sea[x - 1][y - 1][d - 1]:
        sea[x - 1][y - 1][d - 1].plus(1)
    else:
        f = Fish(x - 1, y - 1, d - 1, 1, False)


sx, sy = tuple(map(int, input().split()))

shark = (sx - 1, sy - 1)


def check_smell():
    for i in range(4):
        for j in range(4):
            if smells[i][j]:
                smells[i][j] -= 1


for i in range(S):

    nsea: list[Fish] = [[[None] * 8 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(8):
                if sea[i][j][k]:
                    sea[i][j][k].move()

    check_smell()
    shark = shark_move(shark)
    for i in range(4):
        for j in range(4):
            for nfish in sea[i][j]:
                if nfish == None:
                    continue
                nfish.put()
    sea = nsea

ans = 0
for i in range(4):
    for j in range(4):
        for k in range(8):
            if sea[i][j][k]:
                ans += sea[i][j][k].cnt


print(ans)
