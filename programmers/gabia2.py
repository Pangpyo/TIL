def solution(dots, lines):

    l = len(lines)
    visit = [0] * l
    global answer
    answer = l + 1

    def perm(n, lastdot):
        global answer
        if lastdot >= dots[-1]:
            answer = min(answer, n)
            return
        if n == l:
            return
        nextdot = 0
        for dot in dots:
            if lastdot < dot:
                nextdot = dot
                break
        for i in range(l):
            if visit[i]:
                continue
            visit[i] = 1
            perm(n + 1, nextdot + lines[i])
            visit[i] = 0

    perm(0, 0)
    if answer == l + 1:
        return -1
    else:
        return answer


dots = [1, 8, 12, 20, 30, 40]
lines = [1, 3, 4, 6]

print(solution(dots, lines))
