# 9613 GCD 합 S4

from math import gcd

# 수학
for t in range(int(input())):
    nums = list(map(int, input().split()))
    ans = 0
    for i in range(1, nums[0]):
        for j in range(i + 1, nums[0] + 1):  # 나보다 뒤에 있는 수와의 gcd만 검사
            ans += gcd(nums[i], nums[j])  # gcd 함수를 사용하면 쉽게 구할 수 있음
    print(ans)
