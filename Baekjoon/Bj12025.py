# 12025 장난꾸러기 영훈 G5

def solution() :
    password = input()
    k = int(input())-1
    n = len(password)
    can_changed = [-1]*n
    cnt = 0
    high = [0]*n
    for i in reversed(range(n)) :
        if password[i] in ('1', '2', '6', '7') :
            can_changed[i] = cnt
            cnt += 1
    temp = 0
    for i in range(n) :
        if can_changed[i] >= 0:
            if temp+(1<<can_changed[i]) <= k :
                temp += 1<<can_changed[i]
                high[i] = 1

    if temp == k :
        answer = ''
        for i in range(n) :
            p = password[i]
            if can_changed[i] != -1:
                if high[i] :
                    p = '6' if p in ('1', '6') else '7'
                else :
                    p = '1' if p in ('1', '6') else '2'
            answer += p
        return answer
    else :
        return -1

if __name__ == "__main__" :
    print(solution())