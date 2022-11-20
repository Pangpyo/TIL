import sys


sys.stdin = open("input.txt")


for t in range(1, int(input()) + 1):  # 테스트케이스의 개수만큼 포문 반복
    N, S = map(int, input().split())  # 점의 개수와 시작 점을 입력받음
    nums = list(map(int, input().split()))  # 점들의 위치를 입력받음
    if abs(S - min(nums)) <= abs(S - max(nums)):  # 가장 작은 점과 가장 큰 점중 가까운 점을 먼저 방문한다
        ans = abs(S - min(nums)) + max(nums) - min(nums)  # 가장 작은 점이 더 가까운 경우
    else:
        ans = abs(S - max(nums)) + max(nums) - min(nums)  # 가장 큰 점이 더 가까운 경우
    print(f"#{t} {ans}")
