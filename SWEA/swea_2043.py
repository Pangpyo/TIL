# 2043. 서랍의 비밀번호 D1

p, k = map(int, input().split())

if (p - k) >= 0 :
    print(p-k+1)
else : 
    print(1000+p-k+1)