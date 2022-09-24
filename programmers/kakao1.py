from dateutil.relativedelta import relativedelta
from datetime import datetime

def solution(today, terms, privacies):
    N = len(privacies)
    ty, tm, td = map(int, today.split('.'))
    today = datetime(ty, tm, td)
    dic = {}
    for s in terms :
        S, m = s.split()
        dic[S] = int(m)
    answer = []
    for i in range(1, N+1) :
        date, S = privacies[i-1].split()
        y, m, d = map(int, date.split('.'))
        timeinfo = datetime(y, m, d) + relativedelta(months=dic[S])
        timediff = today-timeinfo
        if timediff.days >= 0 :
            answer.append(i)
        
    
    return answer