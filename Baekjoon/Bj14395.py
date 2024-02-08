# 14395 4연산 G5

from collections import deque


def solution() :
    s, t = map(int, input().split())
    if t == 0 :
        return '-'
    elif s == t :
        return 0
    que = deque()
    o = {0 : '*', 1 : '+', 2 : '/'}
    que.append((s, ""))
    visit = set()
    visit.add(s)
    while que :
        s, op = que.popleft()
        for i, ns in enumerate((s*s, s+s, 1)) :
            if ns in visit :
                continue
            if ns > t :
                continue
            nop = op+o[i]
            if ns == t :
                return nop
            visit.add(ns)
            que.append((ns, nop))

    return -1

if __name__ == "__main__" :
    print(solution())