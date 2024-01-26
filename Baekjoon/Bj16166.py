# 16166 서울의 지하철 G5

from collections import defaultdict, deque

def solution() :
    N = int(input())
    subways = []
    station = defaultdict(list)
    visit = [0]*N
    que = deque()
    for i in range(N) :
        subs = list(map(int, input().split()))[1::]
        for s in subs :
            station[s].append(i)
            if s == 0 :
                que.append((i, 0))
                visit[i] = 1
        subways.append(subs)

    dest = int(input())


    while que :
        sub, d = que.popleft()
        if dest in subways[sub] :
            return d
        for s in subways[sub] :
            for nsub in station[s] :
                if not visit[nsub] :
                    visit[nsub] = 1
                    que.append((nsub, d+1))
    return -1

if __name__ == "__main__" :
    print(solution())