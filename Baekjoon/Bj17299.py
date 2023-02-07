# 17299 오등큰수 G3

from collections import defaultdict

N = int(input())

A = list(map(int, input().split()))

dic = defaultdict(int)

for a in A:
    dic[a] += 1


stack = []
D = [-1] * N
for i in reversed(range(N - 1)):
    stack.append(A[i + 1])
    while stack:
        if dic[stack[-1]] > dic[A[i]]:
            D[i] = stack[-1]
            break
        else:
            stack.pop()

print(*D)
