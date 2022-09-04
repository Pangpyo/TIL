# 2470 두 용액 G5


import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline
N = int(input())

liquid = sorted(list(map(int, input().split())))
for i in range(N) :
    if liquid[i] >= 0 :
        nz = i
        break
a = 0
b = N-1
ans = [liquid[a], liquid[b]]
s = sum(ans)
m = abs(s)
while a-b :
    s = liquid[a]+liquid[b]
    if abs(s) < m :
        ans = [liquid[a], liquid[b]]
        m = abs(s)
    if s == 0 :
        break
    elif s < 0 :
        a += 1
    else :
        b -= 1
print(*ans)


# acid = liquid[0:nz]
# alkali = liquid[nz::]

# def binary_search(list, n) : # 이분탐색을 위한 함수 정의
#     start = 0
#     last = len(list) - 1
#     while start <= last :
#         mid = (start+last)//2
#         if list[mid] == n : return mid
#         elif list[mid] > n : last = mid - 1
#         else : start = mid + 1
#     if last < 0 :
#         last = 0
#     if start >= len(list) :
#         start = len(list)-1
#     ans = start if abs(list[start]-n) < abs(list[last]-n) else last
#     return ans

# s = 2000000001
# ans = (liquid[nz], liquid[nz+1]) if (liquid[nz]+liquid[nz+1]) < abs((liquid[nz-1]+liquid[nz-2])) else (liquid[nz-1], liquid[nz-2])

# if len(acid) < len(alkali) :
#     for ac in acid :
#         idx = binary_search(alkali, -ac)
#         al = alkali[idx]
#         if ac+al == 0 :
#             break
#         if abs(ac+al) < s :
#             ans = (ac, al)
#             s = abs(ac+al)
# else :
#     for al in alkali :
#         idx = binary_search(alkali, -al)
#         ac = acid[idx]
#         if ac+al == 0 :
#             break
#         if abs(ac+al) < s:
#             ans = abs(ac, al)
#             s = abs(ac+al)
# print(*ans)