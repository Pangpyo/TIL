# 30023 전구 상태 바꾸기 G5

from copy import deepcopy


def solution():
    N = int(input())
    lights = [0]*N
    for i, c in enumerate(input()):
        if c == "G":
            lights[i] = 1
        elif c == "B":
            lights[i] = 2
    INF = float('inf')
    answer = INF
    for i in range(3):
        nlights = deepcopy(lights)
        temp = 0
        for j in range(N-2):
            diff = (i - nlights[j]) % 3
            if diff:
                temp += diff
                for k in range(3):
                    nlights[j+k] = (nlights[j+k] + diff)%3
        if nlights[-2] == nlights[-1] == i: 
            answer = min(answer, temp)
    return answer if answer != INF else -1

if __name__ == "__main__":
    print(solution())