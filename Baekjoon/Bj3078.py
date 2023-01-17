# 3078 좋은 친구 G4

import sys
from bisect import bisect_right as br

input = sys.stdin.readline

N, K = map(int, input().split())

f = []

for i in range(N):
    f.append((len(input().rstrip()), i))

f.sort()

fname = [f[i][0] for i in range(N)]
fgrade = [f[i][1] for i in range(N)]

temp = 0
end = 0
ans = 0
for i in range(N):
    if fname[i] != temp:
        temp = fname[i]
        end = br(fname, temp)
    ans += br(fgrade, fgrade[i] + K, i, end) - i - 1

print(ans)
