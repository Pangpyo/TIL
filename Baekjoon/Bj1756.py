# 1756 피자굽기 G5


from bisect import bisect_left


D, N = map(int, input().split())

oven = list(map(int, input().split()))

pizza = list(map(int, input().split()))

for i in range(1, D):  # 오븐에서 윗칸보다 아래에 있는 칸들은 위 칸보다 커도 같은 크기를 가진거나 마찬가지이다.
    if oven[i] > oven[i - 1]:
        oven[i] = oven[i - 1]


oven = oven[::-1]  # bisect 함수 사용을 위해 역순으로 바꿔준다


def answer():
    bottom = -1  # 계산상 -1로 시작한다

    for p in pizza:
        if p > oven[-1]:  # 피자의 크기가 오븐의 입구 크기보다 큰 경우 불가능하므로 0 출력
            return 0
        if p > oven[bottom]:  # 피자의 크기가 현재 피자가 깔려있는 오븐의 바로 위 칸보다 큰 경우 이분탐색으로 맞는 칸을 찾는다
            bottom = bisect_left(oven, p)
        else:  # 같거나 작은 경우 피자를 한칸 쌓는다
            bottom += 1
        if bottom >= D:  # 피자가 오븐의 높이보다 높이 쌓인 경우 불가능하므로 0 출력
            return 0

    return D - bottom  # 오븐의 최상단부터 1이므로 D-bottom


print(answer())
