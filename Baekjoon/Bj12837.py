# 12837 가계부 G1



import sys


def solution() :
    input = sys.stdin.readline
    ans = []
    N, M = map(int, input().split())
    tree = [0] * (N+1)

    def query(i):
        ans = 0
        while i>0 :
            ans += tree[i]
            i -= (i&-i)
        return ans
    
    def update(i, n):
        while i < N+1 :
            tree[i] += n
            i += (i& -i)
    for _ in range(M) :
        a, b, c = map(int, input().split())
        if a == 1 :
            update(b, c)
        else :
            ans.append(str(query(c) - query(b-1)))
    return '\n'.join(ans)

if __name__ == "__main__" :
    print(solution())