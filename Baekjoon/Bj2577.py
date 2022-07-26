# 2577 숫자의 개수 B2
import sys

sys.stdin = open("0_숫자의개수.txt")

A = int(input())  
B = int(input())
C = int(input()) 

N = str(A*B*C) #각 자리의 숫자를 세는 문제이므로, 문자열로 변환하는게 문제 해결이 쉽다고 생각했다.

for i in range(0,10) : # 0~9까지의 수를 세어준다.
    print(N.count('%d'%i)) #for문이 반복 될 때 마다 count함수를 사용해 N안에 포함된 i를 세어준다.