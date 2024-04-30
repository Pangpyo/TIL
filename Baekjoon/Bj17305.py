# 17305 사탕 배달 G4

import sys

def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    candy = [[] for _ in range(6)]
    for _ in range(N):
        t, s = map(int, input().split())
        candy[t].append(s)
    candy[3].sort(reverse=True)
    candy[5].sort(reverse=True)
    c3 = len(candy[3])
    c5 = len(candy[5])
    for i in range(1, c3):
        candy[3][i] += candy[3][i-1]
    for i in range(1, c5):
        candy[5][i] += candy[5][i-1]
    answer = 0
    for f in range(M//5+1):
        th = (M-f*5)//3
        temp = 0
        if f and candy[5]:
            temp += candy[5][min(c5, f)-1]
        if th and candy[3]:
            temp += candy[3][min(c3, th)-1]
        answer = max(answer, temp)
    return answer

if __name__ == "__main__":
    print(solution())