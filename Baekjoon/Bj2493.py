# 2493 탑 G5

n = int(input())

T = list(map(int, input().split()))
stack = []
ans = [0] * n
for i in range(n - 1, -1, -1):
    stack.append((T[i], i))
    while stack and stack[-1][0] < T[i - 1]:
        t, j = stack.pop()
        ans[j] = i

print(*ans)
