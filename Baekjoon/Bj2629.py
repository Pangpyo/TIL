# 2629 양팔저울 G3

N = int(input())

nums = list(map(int, input().split()))

K = int(input())

balls = list(map(int, input().split()))

visit = set()

used = [0] * N

a = 0
can = set()


def dfs(n, cnt):
    for i in range(N):
        if used[i]:
            continue
        nn = nums[i]
        used[i] = 1
        n1 = abs(n - nn)
        n2 = n + nn
        if (n1, cnt + 1) not in visit:
            visit.add((n1, cnt + 1))
            can.add(n1)
            dfs(n1, cnt + 1)
        if (n2, cnt + 1) not in visit:
            visit.add((n2, cnt + 1))
            can.add(n2)
            dfs(n2, cnt + 1)
        if (n, cnt + 1) not in visit:
            visit.add((n, cnt + 1))
            can.add(n)
            dfs(n, cnt + 1)
        used[i] = 0


dfs(0, 0)
ans = []
for ball in balls:
    if ball in can:
        ans.append("Y")
    else:
        ans.append("N")

print(*ans)
