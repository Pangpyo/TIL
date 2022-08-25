# 10451 순열 사이클 S3

import sys


sys.stdin = open('input.txt')
def dfs(nums, n) :
    visit[n] = 1
    if visit[nums[n]] == 0 :
        dfs(nums, nums[n])

for t in range(int(input())) :
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers = [0]+numbers
    visit = [0]*(N+1)
    ans = 0
    for i in range(1, N+1) :
        if visit[i] == 0 :
            dfs(numbers, i)
            ans += 1
    print(ans)