# 1629 곱셈 S1


def solution(x, y, z):
    if y == 1:
        return x % z
    else:
        xy = solution(x, y // 2, z)
        if y % 2 == 0:
            return xy * xy % z
        else:
            return xy * xy * x % z


A, B, C = map(int, input().split())
print(solution(A, B, C))
