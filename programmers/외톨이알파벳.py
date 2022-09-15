# programmers 외톨이 알파벳

input_string="edeaaabbccd"

def solution(input_string):
    dic = {}
    check = ''
    for s in input_string :
        if s not in dic :
            dic[s] = 0
    for s in input_string :
        if check == s :
            continue
        else :
            check = s
            dic[s] += 1
    answer = ''
    for k, v in dic.items() :
        if v >= 2 :
            answer += k
    answer = sorted(answer)
    if not answer :
        answer = 'N'
    answer = ''.join(answer)
    return answer

print(solution(input_string))