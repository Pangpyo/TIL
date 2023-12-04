# 19940 피자 오븐

from collections import deque
import sys


def solution() :
    input = sys.stdin.readline
    T = int(input())
    answers = []
    def find(N) :
        sixty = N//60
        N = N%60
        
        que = deque()
        que.append((0, 0, 0, 0, 0, 0))
        visit = [0]*120
        visit[0] = 1
        d = ((-1, 0, 0, 0, 0, 1),
            (1, 0, 0, 0, 1, 0),
            (-10, 0, 0, 1, 0, 0),
            (10, 0, 1, 0, 0, 0),
            (60, 1, 0, 0, 0, 0),)
        answer = [sixty, 0, 0, 0, 0]
        if not N :
            return answer
        while que :
            n, s, t, mt, o, mo = que.popleft()
            for i in range(5) :
                nn = n + d[i][0]
                ns = s + d[i][1]
                nt = t + d[i][2]
                nmt = mt + d[i][3]
                no = o + d[i][4]
                nmo = mo + d[i][5]
                if nn >= 120 or nn < 0:
                    continue
                if visit[nn] :
                    continue
                if nn == N :
                    answer = [ns+sixty, nt, nmt, no, nmo]
                    return answer
                que.append((nn, ns, nt, nmt, no, nmo))
                visit[nn] = 1
        return answer
    for _ in range(T) :
        N = int(input())
        answers.append(find(N))
    return answers

if __name__ == "__main__" :
    for sol in solution() :
        print(*sol)