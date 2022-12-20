# 11660 구간 합 구하기5 S1


N, M = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(N)]


for i in range(N):
    for j in range(1, N):
        table[i][j] += table[i][j - 1]  # x축에서 누적 합을 구한다

for i in range(1, N):
    for j in range(N):
        table[i][j] += table[i - 1][j]  # y축에서 누적 합을 구한다
# print(table)
for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    xsum = 0  # 해당하는 영역을 제외한 x축에서의 누적 합을 구한다
    ysum = 0  # 해당하는 영역을 제외한 y축에서의 누적 합을 구한다
    xysum = 0  # 위의 두 영역이 겹쳤던 부분의 누적 합을 구한다
    if x1 > 1:
        ysum = table[x1 - 2][y2 - 1]  # 각 영역이 1보다 클 때만 계산한다
    if y1 > 1:
        xsum = table[x2 - 1][y1 - 2]  # 각 영역이 1보다 클 때만 계산한다
    if x1 > 1 and y1 > 1:
        xysum = table[x1 - 2][y1 - 2]  # 각 영역이 1보다 클 때만 계산한다
    # print(table[x2 - 1][y2 - 1], xsum, ysum, xysum)
    ans = (
        table[x2 - 1][y2 - 1] - xsum - ysum + xysum
    )  # 해당 영역에서의 누적합에서 xsum, ysum을 뺀 후 겹치는부분만큰 한번 더해준다
    print(ans)
