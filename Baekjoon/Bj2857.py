# 2857 FBI B3

ans = []
for i in range(1, 6) :
    if 'FBI' in input() :
        ans.append(i)
if ans :
    print(*ans)
else :
    print('HE GOT AWAY!')
