# 1963 소수 경로 G4

from collections import deque
import sys


def solution():
    input = sys.stdin.readline
    T = int(input())
    answer = [0]*T
    MAX = 10000
    is_prime = [1]*(MAX)
    for i in range(2, MAX):
        if not is_prime[i]:
            continue
        for j in range(i*2, MAX, i):
            is_prime[j] = 0
    INF = sys.maxsize
    def bfs(a, b):
        visit = set()
        que = deque()
        que.append((a, 0))
        visit.add(a)
        if a == b:
            return 0
        while que:
            n, cnt = que.popleft()
            nums = [n//1000, (n//100)%10, (n//10)%10, n%10]
            for i in range(4):
                on = nums[i]
                for j in range(10):
                    if i == j == 0 or j == on:
                        continue
                    nums[i] = j
                    nn = 0
                    for k in range(4):
                        nn += nums[k]*(10**(3-k))
                    if nn == b:
                        return cnt+1
                    if is_prime[nn] and nn not in visit:
                        que.append((nn, cnt+1))
                        visit.add(nn)
                nums[i] = on
        return 0
    for t in range(T):
        a, b = map(int, input().split())
        ans = bfs(a, b)
        answer[t] = ans
    return answer

if __name__ == "__main__":
    print(*solution(), sep='\n')
