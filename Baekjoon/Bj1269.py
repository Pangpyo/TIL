# 1269 대칭차집합 S3
import sys

sys.stdin = open('20_대칭차집합.txt')

a, b = map(int, input().split())
A = set(map(int, input().split())) # set를 사용하면 쉽게 풀린다.
B = set(map(int, input().split()))

# print(A-B)
# print(B-A)

print(len(A^B)) # 두 세트형을 ^로 연산하면 대칭 차집합이 구해진다.