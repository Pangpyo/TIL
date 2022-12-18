# 2251 물통 G5


A, B, C = map(int, input().split())
ans = set()
visit = {}


def pour(a, b, B):
    diff = B - b
    if a > diff:
        return a - diff, B
    else:
        return 0, b + a


def dfs(a, b, c):
    global A, B, C

    if a == 0:
        ans.add(c)
    if visit.get((a, b, c), 1):
        visit[(a, b, c)] = 0
        aa, ab = pour(a, b, B)
        dfs(aa, ab, c)
        aa, ac = pour(a, c, C)
        dfs(aa, b, ac)
        bb, ba = pour(b, a, A)
        dfs(ba, bb, c)
        bb, bc = pour(b, c, C)
        dfs(a, bb, bc)
        cc, ca = pour(c, a, A)
        dfs(ca, b, cc)
        cc, cb = pour(c, b, B)
        dfs(a, cb, cc)


dfs(0, 0, C)
ans = sorted(list(ans))
print(*ans)
