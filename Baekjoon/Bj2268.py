# 2268 수들의 합 7
import sys


def solution() :
    input = sys.stdin.readline
    sys.setrecursionlimit(10**8)
    N, M = map(int, input().split())
    nums = [0] * (N+1)
    tree = [0] * (N+1)

    def query(i):
        ans = 0
        while i>0 :
            ans += tree[i]
            i -= (i&-i)
        return ans
    
    def update(i, n):
        diff = n-nums[i]
        nums[i] = n
        while i < N+1 :
            tree[i] += diff
            i += (i& -i)
        
    ans = ""
    for _ in range(M):
        t, a, b = map(int, input().split())
        if t == 0 :
            ans += str(query(max(a, b))-query(min(a, b)-1)) + "\n"
        else :
            update(a, b)
    return ans.rstrip()

if __name__ == "__main__" :
    print(solution())