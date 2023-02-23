from pprint import pprint


def solution(n, m, k):
    global answer
    answer = 0
    D = [[0] * (m + 1) for _ in range(n)]
    for i in range(1, k + 1):
        D[0][i] = 1
    for i in range(1, n):
        for j in range(m + 1):
            for z in range(1, k + 1):
                if j + z <= m:
                    print(i, ":", j, z)
                    D[i][j + z] += D[i - 1][j]
    pprint(D)
    return D[-1][-1] % 1000007


print(solution(3, 6, 3))
