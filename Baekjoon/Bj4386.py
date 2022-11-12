# 4386 별자리 만들기 G3

from math import sqrt
import sys


input = sys.stdin.readline

n = int(input())

parent = [i for i in range(n)]

lines = []

stars = []

for i in range(n):
    stars.append(tuple(map(float, input().split())))


def distance(star1, star2):
    x = abs(star1[0] - star2[0])
    y = abs(star1[1] - star2[1])
    return sqrt(x * x + y * y)


for i in range(n):
    for j in range(i + 1, n):
        lines.append((i, j, distance(stars[i], stars[j])))
lines.sort(key=lambda x: x[2])


def find(x):
    if x == parent[x]:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[max(x, y)] = min(x, y)
        return True
    else:
        return False


ans = 0
for u, v, l in lines:
    if union(u, v):
        ans += l
print("%0.2f" % ans)
