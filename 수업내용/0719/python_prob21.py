# 문제 21. 숫자 뒤집기

n = 1234
n_r = 0
while 1 :
    n_r += n%10
    n = n//10
    if n/10 == 0 :
        break
    n_r = n_r*10
print(n_r)