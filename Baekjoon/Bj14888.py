# 14888 연산자 끼워넣기 S1

from itertools import permutations


N = int(input())

nums = list(map(int, input().split()))

opernum = list(map(int, input().split()))

oper = ['+']*opernum[0]+['-']*opernum[1]+['*']*opernum[2]+['%']*opernum[3]
opers = list(permutations(oper, N-1))


min = 1000000000 # 문제에서 주어진 최대범위와 최소범위
max = -1000000000
for i in opers :
    sum = nums[0]
    for j in range(1, N) :
        if i[j-1] == '+' :
            sum += nums[j]
        elif i[j-1] == '-' :
            sum -= nums[j]
        elif i[j-1] == '*' :
            sum *= nums[j]
        elif i[j-1] == '%' :
            if sum < 0 :
                sum = -(abs(sum) // nums[j])
            else :
                sum //= nums[j]
    min = sum if sum < min else min
    max = sum if sum > max else max
print(max)
print(min)

