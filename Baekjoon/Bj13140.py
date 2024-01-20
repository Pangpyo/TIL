# 13140 Hello World!

from itertools import permutations


def solution() :
    N = int(input())
    for per in permutations(range(10), 7) :
        if per[0] == 0 or per[4] == 0 :
            continue
        A = per[0]*10000 + per[1]*1000 + per[2]*110 + per[3]
        B = per[4]*10000 + per[3]*1000 + per[5]*100 + per[2]*10 + per[6]
        if A + B == N :
            space = " "
            if A+B < 100000 : 
                space *= 2
            answer =  "  " + str(A) + "\n" + "+ " + str(B) + "\n-------\n" + space + str(A+B)
            return answer
    return "No Answer"

if __name__ == "__main__" :
    print(solution())