from copy import deepcopy


from copy import deepcopy


def solution(N, T):
    bit_time = [63, 6, 91, 79, 102, 109, 124, 7, 127, 111]
    time_bit = {63: 0, 6: 1, 91: 2, 79: 3, 102: 4, 109: 5, 124: 6, 7: 7, 127: 8, 111: 9}

    def time_flow(time):
        t = [time_bit[i] for i in time]
        t[3] += 1
        if t[3] == 10:
            t[3] = 0
            t[2] += 1
        if t[2] == 6:
            t[2] = 0
            t[1] += 1
        if t[1] == 10:
            t[1] = 0
            t[0] += 1
        if t[0] == 2 and t[1] == 4:
            t[0] = 0
            t[1] = 0
        return [bit_time[i] for i in t]

    S = [0, 0, 0, 0]
    for i, n in enumerate(N):
        for j, t in enumerate(n):
            if t:
                S[i] |= 1 << j
    Tbit = [bit_time[i] for i in T]
    answer = [[0] * 7 for _ in range(4)]
    while S != Tbit:
        nS = time_flow(S)
        print(S, T)
        for i in range(4):
            for j in range(7):
                if S[i] & (1 << j) != nS[i] & (1 << j):
                    answer[i][j] += 1
        S = deepcopy(nS)

    return answer


N = [
    [1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 0],
    [1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 1],
]
T = [0, 0, 5, 8]

print(solution(N, T))
