# 23878 Lonely Photo G4

def solution():
    n = int(input())
    s = input()

    cnt1, cnt2 = 0, 0
    g, h, L, R = [], [], [], []

    prev = '!'
    for i in range(n):
        if s[i] == 'G':
            if cnt2:
                h.append(cnt2)
            cnt1 += 1
            if prev != 'G':
                cnt2 = 0
            prev = 'G'
            if i == n - 1:
                g.append(cnt1)
        else:
            if cnt1:
                g.append(cnt1)
            cnt2 += 1
            if prev != 'H':
                cnt1 = 0
            prev = 'H'
            if i == n - 1:
                h.append(cnt2)
    if s[0] == 'G':
        L, R = g, h
    else:
        L, R = h, g
    L += [0] * (n - len(L))
    R += [0] * (n - len(R))

    ans = 0
    for i in range(n):
        if L[i]:
            if i >= 1 and R[i - 1]:
                ans += R[i - 1] - 1
            if R[i]:
                ans += R[i] - 1
            if L[i] == 1 and i and R[i - 1] and R[i]:
                ans += R[i - 1] * R[i]
        else:
            break
    for i in range(n):
        if R[i]:
            if L[i]:
                ans += L[i] - 1
            if i < n - 1 and L[i + 1]:
                ans += L[i + 1] - 1
            if R[i] == 1 and L[i] and i < n - 1 and L[i + 1]:
                ans += L[i] * L[i + 1]
        else:
            break

    return ans

if __name__ == "__main__":
    print(solution())