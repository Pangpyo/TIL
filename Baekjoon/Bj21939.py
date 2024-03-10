# 21939 문제 추천 시스템 Ver1 G4

from collections import defaultdict
from heapq import heappop, heappush
import sys

def solution() :
    input = sys.stdin.readline
    N = int(input())
    hard = []
    easy = []
    prob = defaultdict(int)
    for _ in range(N) :
        P, L = map(int, input().split())
        heappush(easy, (L, P, 0))
        heappush(hard, (-L, -P, 0))
        
    
    M = int(input())
    answer = []

    def add(f) :
        P, L = map(int, f[1::])
        heappush(easy, (L, P, prob[P]))
        heappush(hard, (-L, -P, prob[P]))

    def recommend(f) :
        n = int(f[1])
        if n == 1 :
            use = hard
        else :
            use = easy
        while use :
            P = -n*use[0][1]
            if prob[P] == use[0][2]:
                answer.append(P)
                return
            heappop(use)
    def solved(f) :
        P = int(f[1])
        prob[P] += 1
    
    func = {"add" : add, "recommend" : recommend, "solved" : solved}

    for _ in range(M) :
        f = tuple(input().split())
        func[f[0]](f)
    
    return answer

if __name__ == "__main__" :
    print(*solution(), sep='\n')