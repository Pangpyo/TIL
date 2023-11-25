# 카카오 인턴 2번



import sys

def solution(edges):
    sys.setrecursionlimit(10**8)
    answer = [0]*4
    N = 1000001
    outlines = [[] for _ in range(N)]
    inlines = [[] for _ in range(N)]
    nodes = set()
    for u, v in edges :
        outlines[u].append(v)
        inlines[v].append(u)
        nodes.add(u)
        nodes.add(v)
    for i in range(1, N) :
        if len(outlines[i]) >= 2 and len(inlines[i]) == 0 :
            answer[0] = i
    parent = [0]*N

    def find(x) :
        if parent[x] <= 0 :
            return x
        y = find(parent[x])
        parent[x] = y
        return y

    def union(x, y) :
        x = find(x)
        y = find(y)
        if x == y :
            parent[x] -= 1
            return True
        parent[min(x, y)] += parent[max(x, y)]
        parent[max(x, y)] = min(x, y)
        return False
    
    for u, v in edges :
        if u == answer[0] :
            continue
        union(u, v)
    
    for i in nodes :
        if i != answer[0] and parent[i] <= 0 :
            if parent[i] == 0 :
                answer[2] += 1
            elif parent[i] == -1 :
                answer[1] += 1
            elif parent[i] == -2 :
                answer[3] += 1
        
    
    return answer


edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]

print(solution(edges))