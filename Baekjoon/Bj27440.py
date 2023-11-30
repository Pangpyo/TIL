# 27440 1로 만들기 G4

from collections import deque

def solution() :
    N = int(input())
    D = {}
    D[N] = 0 
    que = deque()
    que.append((N))
    while que :
        n = que.popleft()
        if n-1 not in D :
            D[n-1] = D[n] + 1
            que.append(n-1)
        if not n%2 and n//2 not in D :
            D[n//2] = D[n] + 1
            que.append(n//2)
        if not n%3 and n//3 not in D :
            D[n//3] = D[n] + 1
            que.append(n//3)
        if 1 in D :
            break
        
            

    return D[1]

if __name__ == "__main__" :
    print(solution())
