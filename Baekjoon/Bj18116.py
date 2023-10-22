# 18116 로봇 조립 G4

import sys


def solution() :
    input = sys.stdin.readline
    N = int(input())
    answer = []

    parent = [-1]*((10**6)+1)
    def find(x) :
        if parent[x] < 0 :
            return x
        y = find(parent[x])
        parent[x] = y
        return y
    
    def union(x, y) :
        x, y = find(x), find(y)
        if x == y :
            return
        parent[min(x, y)] += parent[max(x, y)]
        parent[max(x, y)] = min(x, y)
    for _ in range(N) :
        temp = input().split()
        if temp[0] == 'I' :
            a, b = map(int, temp[1::])
            union(a, b)
        else :
            c = int(temp[1])
            answer.append(-parent[find(c)])

    return answer

if __name__ == "__main__" :
    print(*solution(), sep='\n')