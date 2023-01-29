# 2613 숫자구슬 G2

N, M = map(int, input().split())

beads = list(map(int, input().split()))

start = max(beads)

end = sum(beads)
ans = [0, []]


def check(div):
    maxdiv = -1
    for i in range(len(div)):
        if maxdiv == -1 and sum(div[i]) == middle:
            maxdiv = i
        elif maxdiv >= 0 and sum(div[i]) == middle and len(div[i]) <= len(div[maxdiv]):
            maxdiv = i
    if maxdiv == -1:
        return div
    divv = []
    diff = M - len(div)
    for i in range(len(div)):
        l = len(div[i])
        if i == maxdiv or diff == 0:
            divv.append(l)
        else:
            while diff and l > 1:
                l -= 1
                diff -= 1
                divv.append(1)
            divv.append(l)

    return divv


while start <= end:
    middle = (start + end) // 2
    temp = []
    t = 0
    div = []
    for i in range(N):
        if t + beads[i] <= middle:
            temp.append(beads[i])
            t += beads[i]
        else:
            div.append(temp)
            cnt = 1
            temp = [beads[i]]
            t = beads[i]
    div.append(temp)
    cnt = len(div)
    if cnt > M:
        start = middle + 1
    else:
        end = middle - 1
        cck = check(div)
        if len(cck) == M:
            ans = middle, cck

print(ans[0])
print(*ans[1])
