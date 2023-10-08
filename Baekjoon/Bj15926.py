# 15926 현욱은 괄호왕이야!! G3

def solution() :
    n = int(input())
    brackets = input()
    D = [0]*n
    for i in range(1, n) :
        if brackets[i] == ")" :
            if brackets[i-1] == "(" :
                temp = 0
                if i-2 >= 0 :
                    temp = D[i-2]
                D[i] = temp + 2
            if D[i-1] and i-D[i-1]-1 >= 0 and brackets[i-D[i-1]-1] == "(":
                temp = 0
                if i-D[i-1]-2 >= 0 :
                    temp = D[i-D[i-1]-2]
                D[i] = max(D[i], 2+D[i-1] + temp)
    return max(D)

if __name__ == "__main__" :
    print(solution())