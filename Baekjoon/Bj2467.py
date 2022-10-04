# 2467 용액 G5

N = int(input())

liquid = list(map(int, input().split()))

a = 0
b = N - 1
ans = [liquid[a], liquid[b]]
s = sum(ans)
m = abs(s)
while a - b:
    s = liquid[a] + liquid[b]
    if abs(s) < m:
        ans = [liquid[a], liquid[b]]
        m = abs(s)
    if s == 0:
        break
    elif s < 0:
        a += 1
    else:
        b -= 1
print(*ans)
