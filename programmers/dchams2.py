def get_time(S):
    answer = [0, 0, 0, 0]
    time = {63: 0, 6: 1, 91: 2, 79: 3, 102: 4, 109: 5, 124: 6, 7: 7, 127: 8, 111: 9}
    for i, s in enumerate(S):
        temp = 0
        for j, t in enumerate(s):
            if not t:
                continue
            temp |= 1 << j
        answer[i] = time[temp]
    return answer


# 다음 단계 solution 함수의 형태를 참고해 주세요.


def get_time(n):
    time = {63: 0, 6: 1, 91: 2, 79: 3, 102: 4, 109: 5, 124: 6, 7: 7, 127: 8, 111: 9}
    if n in time:
        return time[n]
    else:
        return -1


def solution(N):
    S = [0, 0, 0, 0]
    for i, n in enumerate(N):
        for j, t in enumerate(n):
            if t:
                S[i] |= 1 << j
    print(S)
    Scan = [[] for _ in range(4)]

    def combi(n, idx):
        if get_time(n) != -1:
            Scan[a].append(get_time(n))
        for i in range(idx, 7):
            if n & (1 << i):
                continue
            combi(n | (1 << i), i + 1)

    for a in range(4):
        combi(S[a], 0)
    print(Scan)
    idx = 0
    answer = []
    for i, tt in enumerate(Scan[0]):
        if tt > 2:
            continue
        temp = [tt, 0, 0, 0]
        for t in Scan[1]:
            temp[1] = t
            for mm in Scan[2]:
                if mm > 5:
                    continue
                temp[2] = mm
                for m in Scan[3]:
                    temp[3] = m
                    if temp[0] == 2 and temp[1] > 3:
                        continue
                    answer.append(temp)
        answer.sort()
    return answer
