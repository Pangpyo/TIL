# 1074 Z S1

n, r, c = map(int, input().split())
t = 0


def z(n, r, c):
    global t  # t에 값을 더해줌
    if n == 0:  # 사각형의 변이 1개일때 return
        return
    if r < 2 ** (n - 1) and c >= 2 ** (n - 1):  # 4등분 기준 2사분면
        t += (2 ** (n - 1)) ** 2
        c -= 2 ** (n - 1)
    elif r >= 2 ** (n - 1) and c < 2 ** (n - 1):  # 3사분면
        t += 2 * (2 ** (n - 1)) ** 2
        r -= 2 ** (n - 1)
    elif r >= 2 ** (n - 1) and c >= 2 ** (n - 1):  # 4사분면
        t += 3 * (2 ** (n - 1)) ** 2
        r -= 2 ** (n - 1)
        c -= 2 ** (n - 1)
    z(n - 1, r, c)  # 1. 사각형의 범위를 절반씩 줄여감


z(n, r, c)

print(t)
