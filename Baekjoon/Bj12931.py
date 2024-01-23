# 12931 두 배 더하기 G5

from collections import deque


def solution() :
    N = int(input())
    def bfs(x) :
        que = deque()
        que.append((0, 0, 0))
        while que :
            n, o, t = que.popleft()
            if n*2 <= x :
                nt = t+1
                nn = n*2
                if nn == x :
                    return (o, nt)
                que.append((nn, o, nt))
            if n+1 <= x :
                no = o+1
                nn = n+1
                if nn == x :
                    return (no, t)
                que.append((nn, no, t))
        return (0, 0)
    answer = 0
    mt = 0
    for n in map(int, input().split()) :
        if n :
            o, t = bfs(n)
            answer += o
            mt = max(t, mt)
    return answer + mt

if __name__ == "__main__" :
    print(solution())