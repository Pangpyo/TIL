from itertools import combinations_with_replacement

def solution(n, info):
    answer = []
    rions = list(combinations_with_replacement(range(0, 11), n))
    maxscore = 0
    for rion in rions :
        score1 = 0
        score2 = 0
        rioninfo = [0]*(11)
        for r in rion :
            rioninfo[10-r] += 1
        for i in range(11) :
            if info[i] == 0 and rioninfo[i] == 0 :
                continue
            if info[i] >= rioninfo[i] :
                score1 += 10-i
            else :
                score2 += 10-i
        if score2 > score1 and (score2 - score1) >= maxscore:
            maxscore = score2-score1
            answer.append(rioninfo+[score2-score1])
    if answer :
        answer.sort(key = lambda x : (x[11], x[0:11][::-1]))
        print(answer)
        ans = answer[-1][0:11]
    else :
        ans = [-1]
          
    return ans

n = 9
info = [0,0,1,2,0,1,1,1,1,1,1]
print(solution(n, info))