# 2056 작업 G4

import sys


def solution() :
    input = sys.stdin.readline
    N = int(input())
    graph = [[] for _ in range(N+1)]
    times = [0]*(N+1)
    for u in range(1, N+1) :
        nums = tuple(map(int, input().split()))
        times[u] = nums[0]
        for v in nums[2::] :
            graph[u].append(v)

    D = [0]*(N+1)

    def dfs(n) :
        if D[n] :
            return D[n]
        temp = 0
        for nn in graph[n] :
            temp = max(temp, dfs(nn))
        temp += times[n]
        D[n] = temp
        return temp

    for i in range(1, N+1) :
        if not D[i] :
            dfs(i)

    return max(D)

if __name__ == "__main__" :
    print(solution())