# 1926. 간단한 369게임 D2

n = int(input())
for i in range(1,n+1) :
    a = str(i)
    count = 0
    for j in a :
        if (j =='3') or (j == '6') or (j == '9') :
            count += 1
    if count == 0 :
        print(a, end = ' ')
    else :
        print('-'*count, end = ' ')