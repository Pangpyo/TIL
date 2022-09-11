N, K = map(int, input().split())

nums = list(range(1, N+1))
ans = []
a = 0
while nums :
    a += K
    a = (a-1)%len(nums)
    ans.append(nums.pop(a))
print('<', end='')
for a in range(N) :
    print(ans[a], end='')
    if a < N - 1 :
        print(', ', end='')
print('>')
    