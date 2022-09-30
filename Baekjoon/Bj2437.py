# 2437 저울 G2


N = int(input())
weight = sorted(list(map(int, input().split())))
minsum = 1
for num in weight:
    if minsum < num:
        break
    minsum += num
print(minsum)


# def combi(li, n):
#     for i in range(len(li)):
#         if n == 1:
#             yield [li[i]]
#         else:
#             for next in combi(li[i + 1 :], n - 1):
#                 yield [li[i]] + next


# n = 1
# combinums = []
# for i in range(1, N + 1):
#     combinums.append(sorted(combi(weight, i), key=lambda x: sum(x)))
# while 1:
#     isanswer = True
#     bp = False
#     for i in range(1, N + 1):
#         for j in combinums[i - 1]:
#             # print(n, j)
#             if sum(j) == n:
#                 bp = True
#                 isanswer = False
#                 break
#             elif sum(j) > n:
#                 break
#         if bp:
#             break
#     if isanswer:
#         print(n)
#         break
#    n += 1
