# 9084 동전 G5

for t in range(int(input())):
    n = int(input())

    coins = list(map(int, input().split()))

    k = int(input())

    D = [0] * (k + 1)  # 경우의 수를 저장할 리스트
    D[0] = 1  # 0원인 경우는 없지만, 이후의 계산을 위해 1로 지정한다.

    for coin in coins:  # 동전별로 경우의수를 세어준다.
        for i in range(1, k + 1):
            if i - coin >= 0 and D[i - coin] >= 1:
                # 해당 금액 - 해당 동전이 0원 이상이면서 그 경우의 수가 1 이상인 경우
                D[i] += D[i - coin]  # 그 경우의 수들을 모두 D[i]에 더해준다.
    print(D[-1])
