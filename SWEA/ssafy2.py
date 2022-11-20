import sys


sys.stdin = open("input.txt")


for t in range(1, int(input()) + 1):
    N = int(input())  # 수의 개수를 입력받는다
    A = list(map(int, input().split()))  # 수열을 입력받는다
    task = []  # 작업을 실행한 후의 값들을 저장할 리스트
    asum = sum(A)  # 현재 값의 총 합
    for i in range(1, N + 1):
        task.append(max(A[i - 1] + i, i) - A[i - 1])  # 기존의 값과 작업 후의 값의 차이를 저장해준다.
    task.sort(reverse=True)  # 값들을 내림차순으로 정렬한다.
    cnt = 0  # 총 몇번 작업을 해야하는지
    for i in range(N):
        if asum >= 2 * N:  # 합이 2*N보다 커질 경우 종료한다
            break
        asum += task[i]  # 합에 이전 값과 작업 후의 값의 차이를 더해준다.
        cnt += 1  # 작업 회수 + 1
    print(f"#{t} {cnt}")
