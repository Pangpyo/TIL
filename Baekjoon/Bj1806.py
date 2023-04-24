# 1806 부분합 G4

from itertools import accumulate


def solution():
    N, S = map(int, input().split())
    nsum = list(accumulate((map(int, input().split()))))
    if S > nsum[-1]:
        return 0
    if nsum[0] == S:
        return 1
    pre = 0
    post = 1
    ans = N
    while 1:
        s = nsum[post] - nsum[pre]
        if s >= S:
            ans = min(post - pre, ans)
            pre += 1
        elif s < S:
            if post == N - 1:
                break
            post += 1
    return ans


if __name__ == "__main__":
    print(solution())
