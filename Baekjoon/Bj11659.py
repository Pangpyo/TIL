# 11659 구간 합 구하기 4 S3

import sys


sys.stdin = open('input.txt')

input = sys.stdin.readline
# 누적합을 사용해서 시간 복잡도를 사용했음에도 시간초과가 났다.
# 이 문제처럼 입력이 매우 많은 경우에는 sys.stdin.readline을 필수적으로 사용해야만 한다는것을 깨달았다.
N, M = map(int, input().split())

nums = list(map(int, input().split()))
prefix_nums = [0, nums[0]]
for s in range(2, N+1) :
    prefix_nums.append(prefix_nums[-1] + nums[s-1])
# 일반적으로 사용하는데 특정 인덱스~인덱스까지의 합을 sum함수로 구할 경우 시간 복잡도가 높아져
# 시간 초과가 나게 된다. 그래서 누적합을 사용해 시간 복잡도를 낮추었다.
for _ in range(M) :
    i, j = map(int, input().split())
    print(prefix_nums[j]-prefix_nums[i-1])