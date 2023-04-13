# 14002 가장 긴 증가하는 부분 수열4 G4

from bisect import bisect_left as bl

N = int(input())
A = list(map(int, input().split()))
pre = []

idxs = []
for n in A:
    if not pre or n > pre[-1]:
        pre.append(n)
        idxs.append(len(pre) - 1)
    else:
        idx = bl(pre, n)
        pre[idx] = n
        idxs.append(idx)

l = len(pre) - 1
D = [0] * (l + 1)
for i in reversed(range(len(idxs))):
    if idxs[i] == l:
        D[l] = A[i]
        l -= 1
    if l == -1:
        break

print(l + 1)
print(*D)
