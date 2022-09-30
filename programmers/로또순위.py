# 2021 Dev_matching 웹 백엔드 로또의 최고순위와 최저 순위


def solution(lottos, win_nums):
    cnt = 0
    zeros = 0
    for num in lottos:
        if num in win_nums:
            cnt += 1
        if num == 0:
            zeros += 1
    minrank = 6 - cnt + 1 if cnt >= 2 else 6
    maxrank = 6 - (cnt + zeros) + 1 if cnt + zeros >= 2 else 6
    answer = [maxrank, minrank]
    return answer
