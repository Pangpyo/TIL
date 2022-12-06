# 2668 숫자고르기 G5

N = int(input())


nums = [0]


for i in range(1, N + 1):
    nums.append(int(input()))


def dfs(n):
    nn = nums[n]
    if visit[nn] == False:
        visit[nn] = True
        up.add(n)
        down.add(nn)
        dfs(nn)


visit = [False] * (N + 1)
ans = []

for i in range(1, N + 1):
    up = set()
    down = set()
    dfs(i)
    if up == down:
        for x in down:
            ans.append(x)
    # 만약 같지 않다면, 들어온 visited 다시 False로 돌린다.
    else:
        for x in down:
            visit[x] = False
ans.sort()
print(len(ans))
print(*ans, sep="\n")
