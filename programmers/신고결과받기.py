# 프로그래머스 카카오 2022 신고 결과 받기

def solution(id_list, report, k):
    n = len(id_list)
    report = list(set(report))
    reporting = {}
    reported = {}
    for id in id_list :
        reporting[id] = []
        reported[id] = 0
    for r in report :
        reporting_user, reported_user = r.split()
        reporting[reporting_user].append(reported_user)
        reported[reported_user] += 1
    answer = []
    for id, v in reporting.items() :
        cnt = 0
        for n in v :
            if reported[n] >= k :
                cnt += 1
        answer.append(cnt)
    reported = [0]
    
    return answer