# 5431 민석이의 과제 체크하기 D3

import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())

for i in range(1, T+1) : 
    N, K = map(int, input().split()) 
    stu = list(range(1, N+1)) # 모든 학생들의 리스트를 번호로 만든다.
    stu_ass = map(int, input().split()) # 숙제를 제출한 학생을 입력받는다.
    for j in stu_ass : # 모든 학생들의 리스트에서 숙제를 제출한 학생의 번호를 지워준다.
        stu.remove(j)
    print('#%d'%i, *stu)