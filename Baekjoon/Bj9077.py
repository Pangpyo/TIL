# 9077 지뢰제거 G3

from collections import defaultdict
import sys


def solution() :
    input = sys.stdin.readline
    T = int(input())
    answers = [0]*T
    for t in range(T) :
        N = int(input())
        X = set()
        Y = set()
        stars = tuple(tuple(map(int, input().split())) for _ in range(N))
        for x, y, in stars :
            X.add(x)
            Y.add(y)
        X, Y = list(X), list(Y)
        X.sort()
        Y.sort()
        X_list = defaultdict(int)
        Y_list = defaultdict(int)
        for i, x in enumerate(X) :
            X_list[x] = i+1
        for i, y in enumerate(Y) :
            Y_list[y] = i+1
        n, m = len(X), len(Y)
        cnts = [[0]*(m+1) for _ in range(n+1)]
        for x, y in stars :
            cnts[X_list[x]][Y_list[y]] += 1
        for i in range(1, n+1) :
            for j in range(1, m+1) :
                cnts[i][j] += cnts[i-1][j] + cnts[i][j-1] - cnts[i-1][j-1]
        def get_diff(n, list_, N) :
            a = list_[n-1]
            for i in range(11) :
                nn = n + i
                if list_[nn-1] > a + 10 :
                    nn -= 1
                    break
                if nn == N :
                    break
            return nn
        answer = 0
        for x in range(1, n+1) :
            nx = get_diff(x, X, n)
            for y in range(1, m+1) :
                ny = get_diff(y, Y, m)
                temp = cnts[nx][ny] - cnts[x-1][ny] - cnts[nx][y-1] + cnts[x-1][y-1]
                answer = max(answer, temp)
        answers[t] = answer
    return answers

if __name__ == "__main__" :
    print(*solution(), sep='\n')