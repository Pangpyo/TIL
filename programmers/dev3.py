from itertools import product
from typing import Counter


def solution(k):
    matches = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    dic = Counter(matches)
    print(dic)
    maxn = k // 2
    answer = 0
    numbers = set()
    for i in range(1, maxn + 1):
        pro = product(matches, repeat=i)
        for p in pro:
            if sum(p) == k:
                numbers.add(p)
    for numbs in numbers:
        x = 1  # 포기...
    print(numbers)
    return answer


print(solution(11))


# from itertools import product

# def solution(k):
#     matches = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
#     nums = list(range(10))
#     maxn = k // 2
#     answer = 0
#     for i in range(1, maxn + 1):
#         permu = product(nums, repeat=i)
#         for per in permu:
#             nsum = 0
#             for n in per:
#                 nsum += matches[n]
#                 if nsum > k:
#                     break
#             if nsum == k:
#                 answer += 1
#     if k == 1:
#         answer = 0
#     return answer

# 5 :5  6 : 7 11 : 99
