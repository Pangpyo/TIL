# 14888 연산자 끼워넣기 S1

from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))

opernum = list(map(int, input().split()))

oper = ['+']*opernum[0]+['-']*opernum[1]+['*']*opernum[2]+['%']*opernum[3] # 받아준 연산자의 개수를 리스트로 만들어줌
opers = list(permutations(oper, N-1)) # N-1개의 연산자들을 순열을 찾아주는 함수를 이용해 모든 경우의 수를 리스트로 만들어줌


min = 1000000000 # 문제에서 주어진 최대범위와 최소범위
max = -1000000000
for i in opers :
    sum = nums[0]
    for j in range(1, N) : # 각 연산자에 맞게 계산을 해줌. 기존 사칙연산에 상관없이 순서대로 진행
        if i[j-1] == '+' :
            sum += nums[j]
        elif i[j-1] == '-' :
            sum -= nums[j]
        elif i[j-1] == '*' :
            sum *= nums[j]
        elif i[j-1] == '%' :
            if sum < 0 :
                sum = -(abs(sum) // nums[j]) # 문제의 조건에 맞게 음수가 나올 경우 양수로 몫을 구해주고, 음수로 바꿔줌
            else :
                sum //= nums[j]
    min = sum if sum < min else min # 각각 최대값과 최소값을 구해줌
    max = sum if sum > max else max 
print(max) # 출력
print(min)

