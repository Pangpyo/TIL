# 1158 요세푸스 문제4

N, K = map(int, input().split())

peaple = [i for i in range(1, N + 1)]

a = K
n = N
answer = []
while peaple:
    a = (a - 1) % n
    answer.append(peaple.pop(a))
    a += K
    n -= 1

print("<", end="")
for i in range(N):
    if i == N - 1:
        print(f"{answer[i]}>", end=" ")
    else:
        print(f"{answer[i]},", end=" ")
