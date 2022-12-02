# 성격 유형 검사하기


def solution(survey, choices):
    dic = {}
    dic["R"] = 0
    dic["T"] = 0
    dic["C"] = 0
    dic["F"] = 0
    dic["J"] = 0
    dic["M"] = 0
    dic["A"] = 0
    dic["N"] = 0

    N = len(survey)
    for i in range(N):
        if choices[i] > 4:
            dic[survey[i][1]] += choices[i] - 4
        elif choices[i] < 4:
            dic[survey[i][0]] += 4 - choices[i]
    answer = ""
    if dic["R"] >= dic["T"]:
        answer += "R"
    else:
        answer += "T"
    if dic["C"] >= dic["F"]:
        answer += "C"
    else:
        answer += "F"
    if dic["J"] >= dic["M"]:
        answer += "J"
    else:
        answer += "M"
    if dic["A"] >= dic["N"]:
        answer += "A"
    else:
        answer += "N"

    return answer
