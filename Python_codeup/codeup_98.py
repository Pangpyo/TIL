# 6098 : [기초-리스트] 성실한 개미

d = []
for i in range(10) :
    d.append(list(map(int, input().split())))


x, y = [1, 1]

while 1 :
    d[x][y] = 9
    if d[x][y+1] == 0 :
        y += 1
    elif (d[x][y+1] == 1) and d[x+1][y] ==0:
        x += 1
    elif (d[x+1][y] == 1 and d[x][y+1] == 1) :
        break
    elif d[x+1][y] ==2 or d[x][y+1 ==2] :
        if d[x+1][y] ==2 :
            d[x+1][y] = 9
        elif d[x][y+1] ==2 :
            d[x][y+1] = 9
        
        break

for i in range(10) :
    for j in range(10) :
        print(d[i][j], end=" ")
    print('')