# 17298 오큰수 G4


N = int(input())

nums = list(map(int, input().split()))

answer = [-1] * N

stack = []

stack.append(0)
for i in range(1, N):
    while stack and nums[stack[-1]] < nums[i]:
        answer[stack.pop()] = nums[i]
    stack.append(i)

print(*answer)
