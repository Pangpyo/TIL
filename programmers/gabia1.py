from copy import deepcopy


def solution(K, user_scores):
    first_page = []
    dic = {}
    answer = 0
    for i, user_score in enumerate(user_scores):
        user, score = user_score.split()
        score = int(score)
        if user in dic and score <= dic[user][0]:
            continue

        dic[user] = [score, i]
        new_page = sorted(dic.keys(), key=lambda x: (-dic[x][0], dic[x][1]))[0:K]

        if first_page != new_page:
            answer += 1
            first_page = deepcopy(new_page)

    return answer


K = 3
U = ["a 100", "c 200", "b 150", "l 100", "a 120", "b 300", "c 110"]

print(solution(K, U))
