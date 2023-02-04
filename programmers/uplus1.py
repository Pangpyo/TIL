def solution(weight: list):
    weight.sort(reverse=True)
    sw = sum(weight)
    l = len(weight)
    answer = []

    def team1(n, s: list, q):
        if q * 2 > sw:
            return
        if n == l - 2:
            return
        if s:
            team2(0, s, q, 0)
        for i in range(n, l):
            s[i] = 1
            team1(i + 1, s, q + weight[i])
            s[i] = 0

    def team2(n, s: list, q1, q2):
        if q2 > q1:
            return
        elif q2 == q1:
            answer.append((s.count(1), q1))
        else:
            for i in range(n, l):
                if s[i]:
                    continue
                s[i] = 1
                team2(i + 1, s, q1, q2 + weight[i])
                s[i] = 0

    team1(0, [0] * l, 0)
    answer.sort(reverse=True)

    return list(answer[0])


w = [100, 60, 40, 20, 35, 45]
print(solution(w))
