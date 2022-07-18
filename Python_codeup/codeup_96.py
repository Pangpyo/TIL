# 6096 : [기초-리스트] 바둑알 십자 뒤집기


d = []
for i in range(19) :
    d.append(list(map(int, input().split())))

n = int(input())

for a in range(n) :
    x, y = map(int,input().split())
    for j in range(19) :
        if d[j][y-1] == 0 :
            d[j][y-1] = 1
        else :
            d[j][y-1] = 0

        if d[x-1][j] == 0 :
            d[x-1][j] = 1
        else :
            d[x-1][j] = 0

for i in range(19) :
    for j in range(19) :
        print(d[i][j], end=" ")
    print('')