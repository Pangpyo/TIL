# 20437 링고와 순열 G5

from collections import defaultdict, deque
import sys


def solution() :
    input = sys.stdin.readline
    T = int(input())
    answers = ['-1']*T
    for t in range(T) :
        W = input().rstrip()
        K = int(input())
        dic = defaultdict(deque)
        answer = [sys.maxsize, 0]
        for i, w in enumerate(W):
            dic[w].append(i)
            if len(dic[w]) == K :
                temp = dic[w][-1] - dic[w][0] + 1
                answer[0] = min(answer[0], temp)
                answer[1] = max(answer[1], temp)
                dic[w].popleft()
        if answer[1] :
            answers[t] = ' '.join(map(str, answer))
        
    
    return answers

if __name__ == "__main__" :
    print(*solution(), sep='\n')