# 1796 신기한 키보드 G4


def solution():
    inf = float("inf")
    alpha = [[0, inf, 0] for _ in range(26)]

    for i, c in enumerate(input()):
        idx = ord(c) - ord("a")
        alpha[idx][0] += 1
        alpha[idx][1] = min(alpha[idx][1], i)
        alpha[idx][2] = max(alpha[idx][1], i)

    idx = [0, 0]
    pre = [0, 0]
    for i in range(26):
        a, b, c = alpha[i]
        if not a:
            continue
        D = [inf, inf]
        D = [
            min(
                pre[0] + abs(b - idx[0]) + abs(b - c),
                pre[1] + abs(b - idx[1]) + abs(b - c),
            )
            + a,
            min(
                pre[0] + abs(c - idx[0]) + abs(c - b),
                pre[1] + abs(c - idx[1]) + abs(c - b),
            )
            + a,
        ]
        idx = [c, b]
        pre = [*D]
    return min(D)


if __name__ == "__main__":
    print(solution())
