# 9997 폰트 G3

import sys


def solution():
    input = sys.stdin.readline
    N = int(input())

    def change_bit(word):
        temp = 0
        for w in word:
            temp |= 1 << (ord(w) - ord("a"))
        return temp

    nums = [change_bit(input().rstrip()) for _ in range(N)]
    ok = (1 << 26) - 1
    ans = 0

    def bt(n, contain):
        nonlocal ans
        if contain == ok:
            ans += 1
        if n == N:
            return
        for i in range(n, N):
            bt(i + 1, contain | nums[i])

    bt(0, 0)
    return ans


if __name__ == "__main__":
    print(solution())
