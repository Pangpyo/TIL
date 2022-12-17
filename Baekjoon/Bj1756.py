# 1756 피자굽기 G5


from bisect import bisect_left


D, N = map(int, input().split())

oven = list(map(int, input().split()))

pizza = list(map(int, input().split()))

for i in range(1, D):
    if oven[i] > oven[i - 1]:
        oven[i] = oven[i - 1]


oven = oven[::-1]

# print(oven)


def answer():
    bottom = -1

    for p in pizza:
        if p > oven[-1]:
            return 0
        if p > oven[bottom]:
            bottom = bisect_left(oven, p)
        else:
            bottom += 1
        if bottom >= D:
            return 0

    return D - bottom


print(answer())
