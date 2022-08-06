#1003번 피보나치 함수 S3

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

import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1, T+1) :
    fibo = [(1, 0), (0,1), (1, 1)] 
    n = int(input())
    if n > 2 :
        for i in range(3, n+1) :
            fibo.append((fibo[i-2][0]+fibo[i-1][0], fibo[i-2][1]+fibo[i-1][1]))
    print(*fibo[n])
# 동적 프로그래밍을 이용해 해결했다. 각 시도시의 값을 모두 리스트에 저장하면서 진행하면 시간 복잡도를 낮출 수 있다.