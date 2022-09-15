# pccp 모의고사1 체육대회

from itertools import permutations


def solution(ability):
    player = len(ability)
    num = len(ability[0])
    answer = 0
    combi = list(permutations(ability, num))
    for c in combi :
        s = 0
        for i in range(num) :
            s += c[i][i]
        answer = s if s > answer else answer
    return answer

ability = [[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]

print(solution(ability))