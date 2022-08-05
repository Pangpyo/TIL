# 1218 괄호 짝짓기 D4

import sys

sys.stdin = open("_괄호짝짓기.txt")

for i in range(1, 11) :
    l = int(input())
    pars = list(input())
    leftpars = ['{','[','<','('] # 좌괄호
    rightpars = ['}',']','>',')'] # 우괄호
    parcheck = [] # 괄호들이 들어가고 지워질 리스트
    ans = 1
    for par in pars :
        if par in leftpars : # 좌괄호가 나올 경우 parcheck에 append해줌
            parcheck.append(par)
        else : # 우괄호가 나올 경우
            if rightpars.index(par) == leftpars.index(parcheck[-1]) :
                # parcheck의 가짱 끝에 해당 우괄호과 짝이 되는 좌괄호가 있는지 체크
                parcheck.pop()
                # 맞을 경우 짝이 되는 괄호를 pop해줌
            else : # 아닐 경우 유효하지 않으므로 0을 ans에 넣어주고 for문 break
                ans = 0
                break
    print('#%d'%i, ans)