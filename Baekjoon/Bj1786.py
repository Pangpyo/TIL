# 1786 찾기 P5


def failure(s):
    j = 0
    sl = len(s)
    f = [0] * sl
    for i in range(1, sl):
        while j > 0 and s[i] != s[j]:
            j = f[j - 1]
        if s[i] == s[j]:
            j += 1
            f[i] = j
    return f


def solution():
    s = input()
    p = input()
    j = 0
    sl = len(s)
    pl = len(p)
    f = failure(p)
    cnt = 0
    idxs = []
    for i in range(sl):
        while j > 0 and s[i] != p[j]:
            j = f[j - 1]
        if s[i] == p[j]:
            j += 1
        if j == pl:
            idxs.append(i - pl + 2)
            cnt += 1
            j = f[j - 1]
    print(cnt)
    print(*idxs)


if __name__ == "__main__":
    solution()
