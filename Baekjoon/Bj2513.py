# 2513 통학버스 G3

import sys

input = sys.stdin.readline

N, K, S = map(int, input().split())

plus = []
minus = []

for i in range(N):
    d, n = map(int, input().split())  # S를 기준으로 양쪽의 거리를 측정해서 나누어줌
    if d > S:
        plus.append([d - S, n])  # 해당 지점까지의 거리와 그 지점에서 태워야할 학생 수 저장
    elif d < S:
        minus.append([S - d, n])

plus.sort()  # 양쪽의 거리들을 정렬
minus.sort()


def bus(L: list):
    a = 0  # 총 이동 거리
    while L:
        a += L[-1][0]  # 가장 먼 지점까지 다녀옴
        k = K  # 버스에 남은 자리 k자리
        while k and L:  # 해당 지점까지 다녀오면서 k명을 데리고 옴
            if L[-1][1] > k:  # 해당 지점에 있는 학생 수가 k명보다 많은 경우
                L[-1][1] -= k  # 데리고 오면서 그 지점의 학생수를 k명만큼 뻄
                k = 0  # 남은 자리는 0자리
            else:
                k -= L[-1][1]  # 더 적은 경우 해당 지점의 학생 수를 모두 데리고 온 후 그 지점을 리스트에서 pop
                L.pop()

    return a * 2  # 왕복이므로 *2


print(bus(plus) + bus(minus))  # 양쪽으로 다녀옴
