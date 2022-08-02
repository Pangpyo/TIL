# 2750 수정렬하기 B2
import sys

sys.stdin = open('23_수정렬하기.txt')


N = int(input())
A = []
for _ in range(N) : 
    a = int(input())
    A.append(a)

A.sort() #수를 입력받은 후 sort를 이용해 정렬했다.
print(*A, sep='\n') # 한 줄씩 출력했다.