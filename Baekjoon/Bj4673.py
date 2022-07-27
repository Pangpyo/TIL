# 4673 셀프 넘버 S5

for N in range(1,10001) :
    check = 0
    if N < 40 : 
# 10000범위에서 셀프넘버는 그 수보다 36 낮은 수만 검사하면 됨. 시간 감소를 위해 설정하였으며 넉넉하게 40까지 검사함
        for M in range(1, N+1) : 
            m = 0  
            for i in str(M) : #M의 각 자릿수의 합 m을 구함
                m += int(i)
            if M+m == N : #M과 m을 구한 값이 N이 되면 종료(최소값)
                check = 1
                break
    else : 
        for M in range(N-40, N+1) : 
            m = 0  
            for i in str(M) : 
                m += int(i)
            if M+m == N : 
                break
    if check == 0 :
        print(N)
# 시간 복잡도를 낮추기 위해 노력했지만 코드가 길어져버렸다. 더 깔끔한 방법은 없었을까?