# 17220 마약수사대 G4

import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    graph = [[] for _ in range(26)]
    reversed_graph = [[] for _ in range(26)]
    def to_num(A) :
        return ord(A) - ord('A')
    root_list = [0]*26
    for _ in range(M) :
        a, b = map(to_num, input().split())
        graph[a].append(b)
        reversed_graph[b].append(a)
        root_list[b] = 1

    visit = [0]*26
    knows = list(input().split())
    know_list = [0]*26    
    for know in knows[1::] :
        know_list[to_num(know)] = 1
    def dfs(n) :
        visit[n] = 1
        for nn in graph[n] :
            if visit[nn] or know_list[nn] :
                continue
            dfs(nn)

    use = 0
    for i in range(26) :
        if know_list[i] or root_list[i]:
            continue
        dfs(i)
        use += 1

    ans = sum(visit) - use
    return ans

if __name__ == "__main__" :
    print(solution())