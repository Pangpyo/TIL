# 16987 계란으로 계란치기 G5


from itertools import permutations


N = int(input())

eggs = list(tuple(map(int, input().split())) for _ in range(N))
print(eggs)

pers = list(permutations(range(N), N))


for per in pers:
    live = [True] * N
    ok = True
    for i in range(N):
        if per[i] == i:
            ok = False
            break
