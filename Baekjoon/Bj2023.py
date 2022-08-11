# 2023 신기한 소수 G5

# n = int(input())
# M = 10**(n-1) if 10**(n-1) > 2 else 2
# N = 10**(n)

# def prime(a) :
#     if a < 2 :
#         return False
#     for i in range(2, int(a**0.5)+1) :
#         if a%i == 0 :
#             return False
#     return True

# for i in range(M, N) :
#     cnt = 0
#     for j in range(n) :
#         if prime(i//(10**j)) :
#             cnt += 1
#     if cnt == n :
#         print(i)
# 시간 초과가 뜬다.

# import math
# import sys
# input = sys.stdin.readline

# n = int(input())
# M = 10**(n-1) if 10**(n-1) > 2 else 2
# N = 10**(n)-1
# array = [True for _ in range(N)]
# for i in range(2, int(math.sqrt(N))+1) :
#     if array[i] == True :
#         j = 2
#         while i * j < N :
#             array[i*j] = False
#             j += 1
# primenumbers = []
# primenumbers_n = []
# for i in range(2, N) :
#     if array[i] :
#         primenumbers.append(i)
#     if i >= M :
#         primenumbers_n.append(i)

# for i in primenumbers_n :
#     cnt = 0
#     for j in range(n+1) :
#         if i//(10**j) in primenumbers :
#             cnt += 1
#     if cnt == n :
#         print(i)
# 속도는 빠르나 메모리가 초과된다. 메모리 초과는 처음 겪는 일이다.

