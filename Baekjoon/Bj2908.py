# 2908 상수 B2
import sys

sys.stdin = open("1_상수.txt")

A, B = map(str, input().split()) #문자열을 뒤집기 위해 str으로 받았다.

A_r = int(A[::-1])
B_r = int(B[::-1]) # 문자열인 A와 B의 인덱스의 순서를 뒤집어주었고, 정수형으로 바꿔주었다.

print(A_r if A_r>B_r else B_r) # A_r과 B_r중 크기가 큰 것을 출력해주었다.
