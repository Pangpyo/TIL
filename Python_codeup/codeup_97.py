# 6097 [기초-리스트] 설탕과자 뽑기

h, w = map(int, input().split())
hw = []
for i in range(h) :
    hw.append([])
    for j in range(w) :
        hw[i].append(0)

n = int(input())

for i in range(n) :
    l, d, x, y = map(int, input().split())
    if d == 0 :
        for j in range(l) :
            hw[x-1][y-1+j] = 1
    else :
        for j in range(l) :
            hw[x-1+j][y-1] = 1


for i in range(h) :
    for j in range(w) :
        print(hw[i][j], end=" ")
    print('')
