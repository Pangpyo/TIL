# 2635 수 이어가기 S5

N = int(input())
ans = []
for i in range(1, N+1) :
    a = N
    b = i
    nums = [a, b]
    while 1 :
        c = a - b
        if c < 0 :
            ans = nums if len(nums) > len(ans) else ans
            break
        nums.append(c)
        a = b
        b = c

print(len(ans))
print(*ans)