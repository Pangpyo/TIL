# 16165 걸그룹 마스터 준석이 S3

from collections import defaultdict
import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    graph = [defaultdict(str), defaultdict(str)]
    answer = []
    for i in range(N) :
        team = input().rstrip()
        cnt = int(input())
        members = sorted([input().rstrip() for j in range(cnt)])
        graph[0][team] = members
        for member in members :
            graph[1][member] = team
    for i in range(M) :
        name = input().rstrip()
        flag = int(input())
        if flag == 0 :
            answer += graph[0][name]
        else :
            answer.append(graph[1][name])
    return answer

if __name__ == "__main__" :
    print(*solution(), sep="\n")