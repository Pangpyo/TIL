# 2115 갤러리 G5

import sys


def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    gallery = tuple(input().rstrip() for _ in range(N))
    answer = 0
    for i in range(N):
        u, d = 0, 0
        for j in range(M):
            if i >= 1 :
                if gallery[i][j] == 'X' and gallery[i-1][j] == '.': 
                    u += 1
                else :
                    answer += u//2
                    u = 0
            if i < N-1 :
                if gallery[i][j] == 'X' and gallery[i+1][j] == '.':
                    d += 1
                else :
                    answer += d//2
                    d = 0
    for i in range(M):
        u, d = 0, 0
        for j in range(N):
            if i >= 1 :
                if gallery[j][i] == 'X' and gallery[j][i-1] == '.': 
                    u += 1
                else :
                    answer += u//2
                    u = 0
            if i < M-1 :
                if gallery[j][i] == 'X' and gallery[j][i+1] == '.':
                    d += 1
                else :
                    answer += d//2
                    d = 0
    return answer

if __name__ == "__main__":
    print(solution())