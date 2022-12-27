# 11687 팩토리얼 0의 개수 S1

# from collections import defaultdict
# from math import factorial

# L = defaultdict(int)
# for i in range(10):
#     n = factorial(i)
#     cnt = 0
#     while not n % 10:
#         cnt += 1
#         n //= 10
#     L[cnt] += 1

# print(L)

# for i in range(10):
#     print(i, end=" ")
#     print(L[i])

M = int(input())


def answer():
    start = 1
    end = 1000000000
    ans = -1
    while start <= end:
        cnt = 0
        mid = (start + end) // 2
        i = 5
        while i <= mid:
            cnt += mid // i
            i *= 5
        if M <= cnt:
            end = mid - 1
            if cnt == M:
                ans = mid
        else:
            start = mid + 1
    return ans


print(answer())
