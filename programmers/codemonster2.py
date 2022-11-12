# 코드몬스터 2


def solution(k, limits, sockets):
    global answer
    answer = 0
    n = len(sockets)

    def dfs(n):
        global answer
        elec = 0
        for nn in sockets[n - 1]:
            if nn > 0:
                elec += dfs(nn)
                pass
            elif nn == -1:
                elec += k
        while elec > limits[n - 1]:
            elec -= k
            answer += 1
        return elec

    dfs(1)
    return answer


k = 300
limits = [2000, 1000, 3000, 200, 600, 500]

sockets = [
    [2, 3, -1, -1, -1],
    [4, 0, -1, -1, 6],
    [5, 0, 0, 0, 0],
    [-1, 0, 0, 0, 0],
    [-1, -1, -1, -1, -1],
    [-1, -1, 0, 0, 0],
]

print(solution(k, limits, sockets))
