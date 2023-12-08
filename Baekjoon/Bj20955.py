# 20955 민서의 응급 수술 G4 

import sys


def solution() :
    input = sys.stdin.readline 
    N, M = map(int, input().split())
    parents = [-1]*(N+1)

    def find(x) :
        if parents[x] < 0 :
            return x
        y = find(parents[x])
        parents[x] = y
        return y
    
    def union(x, y) :
        x = find(x)
        y = find(y)
        if x == y :
            return True
        parents[min(x, y)] += parents[max(x, y)]
        parents[max(x, y)] = min(x, y)
        return False
    answer = -1
    for _ in range(M) :
        u, v = map(int, input().split())
        if union(u, v) :
            answer += 1
    
    for i in range(1, N+1) :
        if parents[i] < 0 :
            answer += 1

    return answer


if __name__ == "__main__" :
    print(solution())