# 1105 팔 S1

L, R = input().split()

r = len(R)
l = len(L)

ans = 0

if l == r:
    for i in range(l):
        if L[i] == R[i] == "8":
            ans += 1
        if R[i] > L[i]:
            break

print(ans)
