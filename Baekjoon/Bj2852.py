# 2852 NBA 농구

N = int(input())

total = 0

wintime = [0, 0]
score = [0, 0]
goaltime = [0, 0]


def winning_team():
    if score[0] > score[1]:
        return 1
    elif score[1] > score[0]:
        return 2
    else:
        return 0


def get_score(n, time: str):
    n = int(n)
    m, s = time.split(":")
    sec = int(m) * 60 + int(s)
    if winning_team():
        wintime[winning_team() - 1] += sec - goaltime[1]
    score[n - 1] += 1
    if winning_team():
        goaltime[0] = winning_team()
        goaltime[1] = sec  # 골을 넣은 시간


for i in range(N):
    n, time = input().split()
    get_score(n, time)

get_score("0", "48:00")


def timestr(n):
    if n < 10:
        return "0" + str(n)
    else:
        return str(n)


print(timestr(wintime[0] // 60) + ":" + timestr(wintime[0] % 60))
print(timestr(wintime[1] // 60) + ":" + timestr(wintime[1] % 60))
