# programmers pccp 3번 유전법칙
def birth(r, n) :
    if r == 'RR' :
        return 'RR'
    elif r == 'rr' :
        return 'rr'
    else :
        if n == 1 :
            return 'RR'
        elif n == 0 :
            return 'rr'
        else :
            return 'Rr'


def solution(queries):
    answer = []
    for q in queries :
        child = []
        n, p = q
        parent = p
        for i in range(n-1) :
            print(parent)
            child.append(parent%4)
            parent = (parent-1)//4 + 1
        ans = 'Rr'
        for c in child[::-1] :
            ans = birth(ans, c)
            print(c, ans)
        answer.append(ans)
        
    return answer

queries = [[5, 3]]
print(solution(queries))