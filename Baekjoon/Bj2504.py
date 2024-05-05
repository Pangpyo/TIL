# 2504 괄호의 값 G5

def solution():
    stack = []
    temp = 1
    answer = 0
    p = input()
    l = len(p)
    for i in range(l):
        if p[i]=='(':
            temp *= 2
            stack.append(p[i])
        elif p[i]=='[':
            temp *= 3
            stack.append(p[i])
        elif p[i]==')':
            if not stack or stack[-1]!='(':
                return 0
            if p[i-1]=='(': 
                answer += temp
            temp //= 2
            stack.pop()
        elif p[i]==']':
            if not stack or stack[-1]!='[':
                return 0
            if p[i-1]=='[': 
                answer += temp
            temp //= 3
            stack.pop()
    if stack:
        return 0
    return answer

if __name__ == "__main__":
    print(solution())