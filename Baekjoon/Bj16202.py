# 16202 MST게임 G4

def solution() :
    N, M, K = map(int, input().split())
    lines = [tuple(map(int, input().split())) for _ in range(M)]
    ans = [0]*K
    
    def find(x) :
        if parent[x] < 0 :
            return x
        y = find(parent[x])
        parent[x] = y
        return y
    
    def union(x, y) :
        x = find(x)
        y = find(y)
        if x == y :
            return False
        parent[min(x, y)] += parent[max(x, y)]
        parent[max(x, y)] = min(x, y)
        return True

    for k in range(K) :
        parent = [-1]*(N+1)
        temp = 0
        for i in range(k, M) :
            u, v = lines[i]
            if union(u, v) :
                temp += (i+1)
        if parent[1] == -N :
            ans[k] = temp
        else :
            break
    return ans

if __name__ == "__main__" :
    print(*solution())