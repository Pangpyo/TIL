# 12892 생일 선물 G4

import sys


def solution():
    input = sys.stdin.readline
    N, D = map(int, input().split())
    gifts = [tuple(map(int, input().split())) for _ in range(N)]
    gifts.sort()
    s = 0
    temp = gifts[0][1]
    answer = temp
    for e in range(1, N):
        while gifts[e][0] - gifts[s][0] >= D:
            temp -= gifts[s][1]
            s += 1
        temp += gifts[e][1]
        answer = max(answer, temp)
    return answer

if __name__ == "__main__":
    print(solution())