# 2668 숫자고르기 G5

N = int(input())


nums = [0]


for i in range(1, N + 1):
    nums.append(int(input()))


def dfs(n):  # 아래쪽 숫자들에 대해 dfs를 진행한다
    nn = nums[n]
    if visit[nn] == False:
        visit[nn] = True
        first.add(n)  # 그 때 n과 nn을 각각 저장해준다
        second.add(nn)
        dfs(nn)


visit = [False] * (N + 1)
ans = []

for i in range(1, N + 1):
    first = set()
    second = set()
    dfs(i)
    if first == second:  # 같은 경우에만 답에 더해준다.
        for d in second:
            ans.append(d)
    else:  # 다른 경우에는 visit을 초기화시킨다.
        for d in second:
            visit[d] = False
ans.sort()  # 정렬한다
print(len(ans))
print(*ans, sep="\n")  # 한 줄씩 출력
