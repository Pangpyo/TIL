# swea 5215 햄버거 다이어트 D3


from itertools import combinations


for t in range(1, int(input()) + 1):
    N, L = map(int, input().split())
    burgers = []

    ans = 0
    for n in range(N):
        burgers.append(tuple(map(int, input().split())))
    for n in range(1, N + 1):
        coms = combinations(burgers, n)
        for com in coms:
            arr = [0, 0]
            for taste, calorie in com:
                arr[0] += taste
                arr[1] += calorie
            if arr[1] <= L:
                ans = max(ans, arr[0])
    print(f"#{t} {ans}")
