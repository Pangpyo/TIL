def solution(p, b):
    parent = [-1] * len(p)
    print(p)

    def find(x):
        if parent[x] < 0:
            return x
        else:
            y = find(parent[x])
            parent[x] = y
            return y

    def union(p, s):
        p = find(p)
        s = find(s)
        if p != s:
            parent[p] += parent[s]
            parent[s] = p

    for s, p in enumerate(p):
        if p < 0:
            continue
        union(p, s)
    answer = []
    for a in b:
        if parent[a] < 0:
            answer.append(-parent[a])
        else:
            answer.append(0)

    print(parent)
    return answer
