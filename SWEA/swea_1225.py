# 1225 암호생성기 D3

import sys

sys.stdin = open("_암호생성기.txt")

while 1 :
    try :
        i = int(input())
    except :
        break
    password = list(map(int, input().split()))
    point = 0 # break 포인트 설정
    while 1 : 
        for j in range(1, 6) : #1~5까지의 범위 설정
            a = password.pop(0) # 첫번째 인덱스를 pop해줌
            a -= j # pop 해준 값에 j를 빼줌(1~5)
            password.append(a) # 다시 그 값을 리스트에 append해줌
            if a <= 0 : # 그 과정에서 a가 0 이하가 되면 리스트의 마지막 값을 0으로 만든 뒤 브레이크해줌
                password[-1] = 0
                point = 1 # 바깥쪽의 while문도 break해주기 위한 변수
                break
        if point == 1 :
            break
    print('#%d'%i, *password)