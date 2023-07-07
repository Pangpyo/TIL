# 16934 게임 닉네임 G3

import sys


def solution() :
    input = sys.stdin.readline
    N = int(input())
    trie = [{}, 0]
    ans = []
    for _ in range(N) :
        name = list(input().rstrip())
        pre = trie
        flag = True
        for i, n in enumerate(name) :
            if n not in pre[0] :
                pre[0][n] = [{}, 0]
                if flag :
                    ans.append("".join(name[0:i+1]))
                    flag = False
            pre = pre[0][n]
        pre[1] += 1
        if flag :
            if pre[1] > 1 :
                name += [str(pre[1])]
            ans.append("".join(name))
    return ans

if __name__ == "__main__" :
    print(*solution(), sep="\n")  