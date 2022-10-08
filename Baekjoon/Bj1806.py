# 1806 부분합 G4

N, S = map(int, input().split())
nums = list(map(int, input().split()))
nsum = [nums[0]]
if nsum[0] == S:
    print(1)
else:
    for i in range(1, N):
        nsum.append(nums[i] + nsum[i - 1])
    if S > nsum[-1]:
        print(0)
    pre = 0
    post = 1
    ans = N
    while 1:
        s = nsum[post] - nsum[pre]
        if s >= S:
            ans = min(post - pre, ans)
            pre += 1
        elif s < S:
            if post == N - 1:
                break
            post += 1
    print(ans)
