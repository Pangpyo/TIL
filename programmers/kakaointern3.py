from bisect import bisect_left, bisect_right
from itertools import combinations, product


def solution(dice):
    answer = []
    n = len(dice)
    dice_groups = tuple(combinations(range(n), n//2)) # 주사위 조합
    dice_nums = tuple(product(range(6), repeat = n//2)) # 던지는 주사위 눈금 경우의 수들
    dice_groups_cnt = len(dice_groups)
    scores = [[] for _ in range(dice_groups_cnt)]
    for i, dice_group in enumerate(dice_groups) : # 각 조합 별로 나올 수 있는 점수 구하기
        for dice_num in dice_nums :
            temp = 0
            for j, a in enumerate(dice_num) :
                temp += dice[dice_group[j]][a]
            scores[i].append(temp)
        scores[i].sort()
    winrate = [0]*dice_groups_cnt # 각 경우의 수의 승리 개수
    scores_cnt = len(scores[0])
    for i in range(dice_groups_cnt//2) : # 경우의 수중 절반만 봐도 판단 가능
        win = 0
        lose = 0
        for s in scores[i] :
            win += bisect_left(scores[dice_groups_cnt-1-i], s) # 이분탐색으로 값 해당 값보다 작은 점수 개수 구하기
            lose += scores_cnt - bisect_right(scores[dice_groups_cnt-1-i], s) # 이분탐색으로 큰 점수 개수 구하기
        winrate[i] = win
        winrate[dice_groups_cnt-1-i] = lose
    max_win = 0
    for i, win in enumerate(winrate) :
        if win > max_win :
            max_win = win
            answer = list(map(lambda x : x + 1, dice_groups[i]))


    return answer

dice = [[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]

print(solution(dice))