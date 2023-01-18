# 12101 1, 2, 3 더하기2

N, K = map(int, input().split())

cnt = 0

nums = [1, 2, 3]

ans = []


def dfs(l: list):  # 백트레킹을 위한 dfs
    global cnt
    global ans
    n = sum(l)
    for nn in nums:
        if n + nn == N:  # 값의 총 합이 N일때
            cnt += 1  # cnt += 1
            if cnt == K:  # 만약 cnt가 K면 ans 입력
                ans = l + [nn]
            continue  # 컨티뉴
        elif n + nn > N:
            continue  # N을 넘어도 컨티뉴
        else:  # N미만일때
            dfs(l + [nn])  # 늘어난 리스트로 다시 dfs


dfs([])
if ans:
    print(*ans, sep="+")
else:
    print(-1)
