#1003번 피보나치 함수

# count_0 = 0
# count_1 = 0
# n = int(input())
# def fibonacci(n) :
#     global count_0, count_1
#     if n == 0 :
#         count_0 +=  1
#         return 0
#     elif n == 1 :
#         count_1 +=  1
#         return 1
#     else :
#         return fibonacci(n-1) + fibonacci(n-2)
# fibonacci(n)
# print(count_0, count_1)
# 주어진 함수를 이용해 전역변수로 해결해 보려 했으나 시간복잡도가 높아 주어진 시간을 초과하였다.

# import sys

# sys.stdin = open("input.txt", "r")

# T = int(input())
# for i in range(1, T+1) :
