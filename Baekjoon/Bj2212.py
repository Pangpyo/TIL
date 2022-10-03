# 2212 센서 G5

N, K = int(input()), int(input())

sensors = sorted(list(map(int, input().split())))
dis = []
if K >= N:
    print(0)
else:
    for i in range(0, N - 1):
        dis.append(sensors[i + 1] - sensors[i])
dis.sort()
print(sum(dis[0 : -1 - (K - 1)]))
