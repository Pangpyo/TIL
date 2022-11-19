# 3234 준환이의 양팔저울 D4

from itertools import permutations, product


for t in range(1, int(input()) + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    per = list(permutations(nums, N))
    LR = list(product([0, 1], repeat=N))
    print(LR)
    ans = 0
    for p in per:
        for lr in LR:
            ok = True
            left = 0
            right = 0
            for i in range(N):
                if lr[i] == 0:
                    left += p[i]
                else:
                    right += p[i]
                if right > left:
                    ok = False
                    break
            if ok:
                ans += 1
    print(f"#{t} {ans}")
