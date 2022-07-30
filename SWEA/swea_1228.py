# 1228. [S/W 문제해결 기본] 8일차 - 암호문1 D3

import sys

sys.stdin = open("_암호문1.txt")



for i in range(1, 11) :
    n = int(input())
    org_pass = input().split() # 원래의 패스워드
    a = int(input())
    comm = list(input().split()) # 명령어 
    for j in range(len(comm)) :
        if comm[j] == 'I' : # 'I'를 기준으로 명령어를 나눈다.
            x = int(comm[j+1])  # 'I' 바로 다음 나온 숫자는 x

            y = int(comm[j+2]) # 'I' 2 번째 뒤의 숫자는 y

            s = comm[j+3:j+3+y] # y다음부터 y개의 숫자들은 s
            
            org_pass = org_pass[0:x] + s + org_pass[x:n] #x번째 항 다음에 s를 끼워넣었다.
    org_pass = org_pass[0:10] # 결과물의 10번째 항까지만 저장한다.
    print('#%d'%i, *org_pass)