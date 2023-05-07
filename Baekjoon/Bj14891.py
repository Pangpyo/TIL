# 14891 톱니바퀴 G5

import sys


def solution():
    input = sys.stdin.readline

    gears = [input().rstrip() for _ in range(4)]

    K = int(input())

    R = [0] * 4

    def teeth(n):
        if n >= 8 or n <= -8:
            return n % 8
        else:
            return n

    def rotate(n, c, d):
        if n + 1 < 4:
            if d == -1:
                pass
            elif gears[n][teeth(2 - R[n])] != gears[n + 1][teeth(6 - R[n + 1])]:
                rotate(n + 1, -c, 1)
        if n - 1 >= 0:
            if d == 1:
                pass
            elif gears[n][teeth(6 - R[n])] != gears[n - 1][teeth(2 - R[n - 1])]:
                rotate(n - 1, -c, -1)
        R[n] = teeth(R[n] + c)

    for _ in range(K):
        n, c = map(int, input().split())
        rotate(n - 1, c, 0)

    ans = 0
    for i in range(4):
        if gears[i][-R[i]] == "1":
            ans += 1 << (i)

    return ans


if __name__ == "__main__":
    print(solution())
