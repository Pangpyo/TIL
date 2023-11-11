# 9011 순서 G5

import sys


def solution() :
    input = sys.stdin.readline
    T = int(input())
    answer = []
    for _ in range(T) :
        N = int(input())
        order = list(map(int, input().split()))
        use = [0]*N
        temp = [-1]*N
        for i in reversed(range(N)) :
            cnt = 0
            for j in range(N) :
                if use[j] :
                    continue
                if cnt == order[i] :
                    temp[i] = j+1
                    use[j] = 1
                    break
                cnt += 1
            if temp[i] == -1:
                temp = ["IMPOSSIBLE"]
                break
        answer.append(' '.join(map(str, temp)))
        
    return answer 

if __name__ == "__main__" :
    print(*solution(), sep='\n')