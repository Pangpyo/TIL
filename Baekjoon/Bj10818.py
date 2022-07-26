# 110818 최소, 최대 B3

N = int(input())

A = list(map(int, input().split()))
min_A = 1000000 # 문제에서 주어진 수의 범위
max_A = -1000000

for i in A :  #min와 max함수를 사용하지 않고 구해보았다.
    if i >= max_A :
        max_A = i
    if i <= min_A :
        min_A = i
        
print(min_A, max_A)