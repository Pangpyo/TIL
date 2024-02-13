# 5021 왕위 계승 G4

from collections import defaultdict
import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    king = input().rstrip()
    tree = defaultdict(list)
    for _ in range(N) :
        a, b, c = input().split()
        tree[a].append(b)
        tree[a].append(c)
    answer = ""
    blood = 0
    def dfs(name, n) :
        if name == king :
            return 1/(1<<n)
        temp = 0
        for parent in tree[name] :
            temp += dfs(parent, n+1)
        return temp

    for _ in range(M) :
        p = input().rstrip()
        nblood = dfs(p, 0)
        if nblood > blood :
            blood = nblood
            answer = p
    return answer

if __name__ == "__main__" :
    print(solution())