# 11729 하노이 탑 이동 순서 S1

import sys


N = int(input())


ans = []


def hanoi(n, start, mid, end):
    if n > 1:
        hanoi(n - 1, start, end, mid)  # 위에 있는 나머지를 빈칸에 옮긴다
        ans.append((start, end))  # 마지막 하나를 원하는 위치로 옮긴다
        hanoi(n - 1, mid, start, end)  # 빈칸에 옮겨놓은 나머지들을 다시 원하는 위치로 가져온다
    else:  # n이 1일때는 재귀하지 않음
        ans.append((start, end))  # 원하는 위치로 옮기기만 한다


hanoi(N, 1, 2, 3)

print(len(ans))
for a, b in ans:
    sys.stdout.write(" ".join([str(a), str(b), "\n"]))
