# 2920 음계 B2

A = list(map(int, input().split()))
ascending = list(range(1,9))
descending = list(range(8,0,-1))

if A == ascending :
    print('ascending')
elif A == descending :
    print('descending')
else :
    print('mixed')