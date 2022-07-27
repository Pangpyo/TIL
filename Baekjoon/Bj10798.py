# 10798 세로읽기 B1

import sys

sys.stdin = open("input.txt")
A = []
l = 0
for i in range(5) :
    a = input()
    A.append(a)
    l = len(a) if len(a) > l else l #받은 줄중 가장 길이가 긴 줄의 길이 저장

for i in range(l) :

    for j in range(5) :  
        try :  #try를 통해 인덱스를 넘어가도 패스
            print(A[j][i], end='')
        except : pass
