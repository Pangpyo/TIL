from math import ceil


fees = 	[1, 461, 1, 10]

records = ["00:00 1234 IN"]

def solution(fees, records):
    dic = {}
    for record in records :
        t, number, cg = record.split()
        h, m = map(int, t.split(':'))
        if number not in dic :
            dic[number] = [cg, (h, m), 0]
        else :
            dic[number][0] = cg
            if cg == 'IN' :
                dic[number][1] = (h, m)
            else :
                ih, im = dic[number][1]
                dic[number][2] += (h-ih)*60+(m-im)
                dic[number][1] = 0
    for k, v in dic.items() :
        if v[0] == 'IN' :
            ih, im = v[1]
            v[2] += (23-ih)*60+(59-im)
            v[1] = 0
    dic = sorted(dic.items(), key = lambda x : int(x[0]))
    answer = []
    for k, v in dic :
        if v[2] <= fees[0] :
            fee = fees[1]
        else :
            fee = fees[1] + ceil((v[2]-fees[0])/fees[2])*fees[3]
        answer.append(fee)
    return answer


print(solution(fees, records))