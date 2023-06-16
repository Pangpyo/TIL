# 2550 전구 G3

from bisect import bisect_left as bl


def solution() :
    N = int(input())
    s = list(map(int, input().split()))
    b = list(map(int, input().split()))
    dic = {}
    for i, n in enumerate(b) :
        dic[n] = i
    A = [0]*N
    for i, n in enumerate(s) :
        A[i] = dic[n]
    pre = []
    D = []
    idxs = []
    for i, n in enumerate(A):
        if not pre or n > pre[-1]:
            pre.append(n)
            idxs.append(len(pre) - 1)
        else:
            idx = bl(pre, n)
            pre[idx] = n
            idxs.append(idx)

    l = len(pre) - 1
    for i in reversed(range(len(idxs))):
        if idxs[i] == l:
            D.append(b[A[i]])
            l -= 1
        if l == -1:
            break
    print(len(D))
    print(*sorted(D))

if __name__ =="__main__" :
    solution()