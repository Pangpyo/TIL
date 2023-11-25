# 카카오 인턴 1번

from collections import defaultdict

def solution(friends, gifts):
    exchanges = {}
    answer = 0
    score = defaultdict(int)
    predict = defaultdict(int)
    N = len(friends)
    for friend in friends :
        exchanges[friend] = defaultdict(int)
    for gift in gifts :
        A, B = gift.split()
        exchanges[A][B] += 1
        score[A] += 1
        score[B] -= 1
    for i in range(N) :
        give = friends[i]
        for j in range(i+1, N) :
            receive = friends[j]
            if give == receive :
                continue
            weight = exchanges[give][receive] - exchanges[receive][give]
            cnt = score[give] - score[receive]
            if weight > 0 :
                predict[give] += 1
            elif weight == 0 :
                if cnt > 0 :
                    predict[give] += 1
                elif cnt < 0 :
                    predict[receive] += 1
            else :
                predict[receive] += 1
    print(predict)
    for k, v in predict.items() :
        answer = max(answer, v)
    return answer


friends = ["muzi", "ryan", "frodo", "neo"]

gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

print(solution(friends, gifts))