# 9019 DSLR G4


from collections import deque
import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline
def calD(n) :
    return 2*n%10000

def calS(n) :
    ans = 9999 if n == 0 else n-1
    return ans

def calL(n) :
    ans = (n%1000)*10 + (n//1000)
    return ans

def calR(n) :
    ans = (n%10)*1000 + (n//10)
    return ans


def bfs(a, b) :
    que = deque([(a)])
    while 1 :
        n = que.popleft()
        if n == b :
            return visit[n]
        if not visit[calD(n)] and n != 0 :
            que.append((calD(n)))
            visit[calD(n)] = visit[n] + 'D'
        if not visit[calS(n)] :
            que.append((calS(n)))
            visit[calS(n)] = visit[n] + 'S'
        if not visit[calL(n)] :
            que.append((calL(n)))
            visit[calL(n)] = visit[n] + 'L'
        if not visit[calR(n)] :
            que.append((calR(n)))
            visit[calR(n)] = visit[n] + 'R'


for _ in range(int(input())) :
    visit = ['']*(10000)
    A, B = map(int, input().split())
    print(bfs(A, B))
