# 25391 특별상 G5

import sys


def solution() :
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    scores = [tuple(map(int, input().split())) for i in range(N)]
    scores.sort(key = lambda x : x[1])
    ans = 0
    for i in range(K) :
        temp = scores.pop()
        ans += temp[0]

    scores.sort(key = lambda x : x[0])
    for i in range(M) :
        temp = scores.pop()
        ans += temp[0]

    return ans

if __name__ == "__main__" :
    print(solution())