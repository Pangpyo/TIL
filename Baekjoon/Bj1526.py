# 1526 가장 큰 금민수 B1

N = int(input())
num47 = 0
for n in range(1, N+1) :
    no = 0
    for i in str(n) :
        if i not in  ['4','7'] :
            no = 1
            break
    if no == 0 :
        num47 = n
print(num47)