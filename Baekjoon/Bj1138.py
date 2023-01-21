# 1138 한 줄로 서기 S2

N = int(input())

P = list(map(int, input().split()))
visit = [0] * N


def dfs(height: list):  # 완전탐색, 백트레킹으로 풀이
    if len(height) == N:  # 길이가 N인 리스트가 완성되면 그것이 답
        return height
    for i in range(N):
        cnt = 0
        if visit[i]:  # 방문 한 경우 컨티뉴
            continue
        for h in height:  # 그 동안 쌓아온 리스트에
            if h > i + 1:  # 나보다 키가 큰 사람이 몇명인지
                cnt += 1
        if cnt == P[i]:  # 그 사람들의 수가 P[i]명이면 ok
            visit[i] = 1  # 방문 후
            ans = dfs(height + [i + 1])  # dfs처리
            if ans:  # return이 있을 경우
                return ans  # return
            visit[i] = 0  # 다시 방문을 0으로 되돌림
    return 0


print(*dfs([]))
