# swea 5789 현주의 상자바꾸기 D3

for t in range(1, int(input()) + 1):
    N, Q = map(int, input().split())
    boxes = [0] * N
    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        for j in range(L - 1, R):
            boxes[j] = i
    print(f"#{t}", end=" ")
    print(*boxes)
