# 16637 괄호 추가하기 G3

def solution() :
    N = int(input())
    E = input()
    answer = -float('inf')
    brasket = [0]*N
    E += '+'
    def cal(a, c, b):
        if c == '+' :
            return int(a)+int(b)
        elif c == '-' :
            return int(a)-int(b)
        else :
            return int(a)*int(b)
        
    def result() :
        res = 0
        temp = 0
        flag = False
        for i in range(0, N, 2) :
            if flag :
                flag = False
                continue
            temp = int(E[i])
            if brasket[i] :
                temp = cal(temp, E[i+1], E[i+2])
                
                flag = True
            res = cal(res, E[i-1], temp)
            temp = 0
        return res

    def dfs(n):
        nonlocal answer
        if n >= N - 1:
            answer = max(answer, result())
            return
        for i in range(n, N-1, 2) :
            dfs(i+4)
            brasket[i] = 1
            dfs(i+4)
            brasket[i] = 0
    dfs(0)
    return answer

if __name__ == "__main__" :
    print(solution())