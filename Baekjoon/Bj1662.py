# 1662 압축 G5

def solution() :
    S = list(input().rstrip())
    stack = []
    l = 0
    temp = ''
    for s in S :
        if s == "(" :
            stack.append((temp, l-1))
            l = 0
        elif s == ")" :
            pre, q = stack.pop()
            l = (int(pre)*l)+q
        else :
            l += 1
            temp = s
    return l

if __name__ == "__main__" :
    print(solution())