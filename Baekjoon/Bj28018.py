# 28018 시간이 겹칠까? G5

from itertools import accumulate
import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    MAX = 1_000_000
    time = [0]*(MAX+2)
    for _ in range(N):
        s, e = map(int, input().split())
        time[s] += 1
        time[e+1] -= 1
    ps = tuple(accumulate(time))
    Q = int(input())
    questions = tuple(map(int, input().split()))
    answer = tuple(ps[questions[i]] for i in range(Q))
    return answer

if __name__ == "__main__":
    print(*solution(), sep='\n')