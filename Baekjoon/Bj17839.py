# 17839 Baba is Rabbit G5

from collections import defaultdict
import sys


def solution():
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    N = int(input())
    graph = defaultdict(list)
    for _ in range(N):
        a, b = input().rstrip().split(" is ")
        graph[a].append(b)
    visit  = defaultdict(int)
    answer = []
    def dfs(x):
        visit[x] = 1
        for xx in graph[x]:
            if not visit[xx]:
                answer.append(xx)
                dfs(xx)
    dfs("Baba")
    answer.sort()
    return answer

if __name__ == "__main__":
    print(*solution(), sep='\n')