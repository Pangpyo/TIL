# 9177 단어 섞기 G4

import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    answers = []
    for i in range(1, N+1):
        a, b, c = input().split()
        al = len(a)
        bl = len(b)
        D = [[-1]*(bl+1) for _ in range(al+1)]
        def dfs(x, y):
            if (x, y) == (al, bl):
                return 1
            if D[x][y] != -1:
                return D[x][y]
            if x < al and a[x] == c[x+y] and dfs(x+1, y):
                D[x][y] = 1
            elif y < bl and b[y] == c[x+y] and dfs(x, y+1):
                D[x][y] = 1
            else:
                D[x][y] = 0
            return D[x][y]
        if dfs(0, 0):
            ans = 'yes'
        else :
            ans = 'no'
        answers.append(f'Data set {i}: {ans}')
    return answers

if __name__ == "__main__":
    print(*solution(), sep='\n')