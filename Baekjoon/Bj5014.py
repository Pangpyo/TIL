# 5014 스타트링크 S1

from collections import deque

F, S, G, U, D = map(int, input().split())


que = deque()
que.append((S, 0))

visit = [0] * (F + 1)
visit[S] = 1


def answer():
    if S == G:  # 시작점과 끝점 층이 같은 케이스... 이거 때문에 계속 틀림
        return 0
    while que:
        s, d = que.popleft()
        if s + U <= F and not visit[s + U]:
            if s + U == G:
                return d + 1
            visit[s + U] = 1
            que.append((s + U, d + 1))

        if s - D >= 1 and not visit[s - D]:  # 최하 1층이므로 1 이상일때! 이거 때문에 계속 틀림
            if s - D == G:
                return d + 1
            visit[s - D] = 1
            que.append((s - D, d + 1))
    return "use the stairs"


print(answer())
