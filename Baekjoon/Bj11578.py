# 11578 팀원 모집 G5

import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())

    prob = [0]*N
    students = []
    for _ in range(M) :
        students.append(list(map(lambda x : int(x)-1, input().split()))[1::])
    inf = sys.maxsize
    ans = inf
    def choose(n, cnt) :
        nonlocal ans
        flag = True
        for i in range(N) :
            if not prob[i] :
                flag = False
                break
        if flag :
            ans = min(ans, cnt)
            return
        for i in range(n, M) :
            for p in students[i] :
                prob[p] += 1
            choose(n+1, cnt+1)
            for p in students[i] :
                prob[p] -= 1
    choose(0, 0)
    return ans if ans != inf else -1


if __name__ == "__main__" :
    print(solution())