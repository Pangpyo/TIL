# 2231 분해합 B2

N = int(input())

for M in range(1, N+1) :
    m = 0 
    for i in str(M) : #M의 각 자릿수의 합 m을 구함
        m += int(i)
    if M+m == N : #M과 m을 구한 값이 N이 되면 종료(최소값)
        print(M)
        break
else :
    print(0)
    
