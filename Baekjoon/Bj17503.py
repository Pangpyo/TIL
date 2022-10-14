# 17503 맥주 축제 S2

from collections import deque
import heapq
import sys


input = sys.stdin.readline

sys.stdin = open("input.txt")

N, M, K = map(int, input().split())
beer = []
for i in range(K):
    v, c = map(int, input().split())
    beer.append((c, v))  # 도수, 선호도 순으로 정렬하기 위해 순서를 바꿔 넣었다.
beer.sort()
beer = deque(beer)


def solution(N, M, beer: deque):
    liver = 0  # 간수치
    drink = []  # 마신 맥주들의 선호도들이 들어갈 힙
    total = 0  # 마신 맥주의 선호도 합
    while beer:
        c, v = beer.popleft()
        if len(drink) < N:  # 맥주를 N개 이하로 마셨을 경우
            heapq.heappush(drink, v)  # 맥주를 하나 마시고, 맥주 목록에 선호도를 힙푸쉬한다.
            total += v  # 선호도의 총 합
        else:
            total -= heapq.heappop(drink)  # 맥주를 N개 이상 마신 경우 가장 선호도가 낮은 맥주를 하나 빼고
            heapq.heappush(drink, v)  # 다음 맥주를 마신다.
            total += v  # 선호도의 총 합
        if total >= M and len(drink) == N:  # 만약 선호도의 총 합이 M을 넘기고, 마신 맥주의 수도 N이라면
            liver = c  # 간수치를 결정한 후 종료한다.
            break
    if total >= M:
        return liver
    else:  # 만약 와일문이 종료 된 후에도 선호도를 채우지 못했다면 -1을 출력한다.
        return -1


print(solution(N, M, beer))
