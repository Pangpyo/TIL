# 2671 잠수함식별 G5

import re


def solution() :
    signal = input()
    check = re.fullmatch(r'(100+1+|01)+', signal)
    if check :
        return "SUBMARINE"
    else :
        return "NOISE"

if __name__ == "__main__" :
    print(solution())