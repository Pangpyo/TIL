# 11964 Fruit Feast G5

from collections import deque


def solution() :
    T, A, B = map(int, input().split())
    que = deque()
    que.append((0, False))
    visit = [0]*(T+1)
    answer = 0
    visit[0] = 1
    while que :
        n, can = que.popleft()
        answer = max(n, answer)
        for nn in (n+A, n+B) :
            if nn > T or visit[nn] :
                continue
            visit[nn] = 1
            que.append((nn, can))
        if not can and not visit[n//2]:
            visit[n//2] = 1
            que.append((n//2, True))
    return answer

if __name__ == "__main__" :
    print(solution())