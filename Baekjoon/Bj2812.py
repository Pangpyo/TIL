# 2812 크게만들기 G3


N, K = map(int, input().split())

num = list(map(int, list(input())))
d = 0
ans = [num[0]]

delete = 0


def change(n):
    global delete, K
    if delete == K:
        return
    if ans and n > ans[-1]:
        ans.pop()
        delete += 1
        change(n)


for i in range(1, N):
    change(num[i])
    ans.append(num[i])
    if delete == K:
        d = i + 1
        break


if d:
    ans = ans + num[d::]
else:
    ans = ans[0 : N - K]
print(*ans, sep="")
