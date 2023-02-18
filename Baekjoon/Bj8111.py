# 8111 0과 1 P5

from collections import deque


T = int(input())


def make_num():
    que = deque([1])
    visit = [""] * (N + 1)
    visit[1] = "1"
    while que:
        n = que.popleft()
        for num in [0, 1]:
            nn = (n * 10 + num) % N
            temp = "".join([visit[n], str(num)])
            if not nn:
                return temp
            if visit[nn] or len(visit[nn]) == 100:
                continue
            visit[nn] = temp
            que.append(nn)
    return "BRAK"


for i in range(T):
    N = int(input())
    print(make_num())
