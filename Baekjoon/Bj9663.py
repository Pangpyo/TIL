# 9663 N-Queen G4

N = int(input())


Q = [0] * N
ans = 0


def place(x):
    for i in range(x):
        if Q[x] == Q[i] or abs(Q[x] - Q[i]) == abs(x - i):
            return False
    return True


def dfs(x):
    global ans
    if x == N:
        ans += 1
        return
    for i in range(N):
        Q[x] = i
        if place(x):
            dfs(x + 1)


dfs(0)

print(ans)
