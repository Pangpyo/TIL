# 1065 한수 S4

def hansu(N) : # 한수를 판별하는 함수 정의
    if N <= 99 :  # 99 이하의 수는 모두 한수이다.
        return 1
    else :
        Sn = str(N)
        if int(Sn[0]) - int(Sn[1]) == int(Sn[1]) - int(Sn[2]) : #주어진 문제는 1000 이하의 수이므로 3자리만 검사
            return 1
        else : 
            return 0
            

N = int(input())
H_count = 0
for i in range(1,N+1) : #주어진 수 이하의 모든 수를 위에서 정의한 함수로 검사
    H_count += hansu(i) #위의 함수는 한수이면 1을 출력한다. 1부터 주어진 수까지 함수를 이용해 카운트를 늘려간다

print(H_count) 