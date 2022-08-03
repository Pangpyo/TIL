# 4949 균형잡힌 세상 S4

import sys


sys.stdin = open('input.txt')
par_left = ['(','[']


while 1 :
    sentence = input()
    pars = []
    YorN = 0
    if sentence == '.' :
        break
    for char in sentence :
        if char in par_left :
            pars.append(char) # 왼괄호들이 나올 경우 리스트에 저장
        if char == ')' : # 오른괄호들이 나올 경우  조건문 실행
            if len(pars) == 0 : # 첫 괄호가 오른괄호일 경우 no
                YorN += 1
                break
            elif pars[-1] == '[' : # 직전 괄호와 짝이 맞지 않을 경우 no
                YorN += 1
                break
            elif pars[-1] == '(' : # 짝이 맞을 경우 괄호 리스트에서 짝이 맞는 괄호를 지워줌
                pars.pop()
        elif char == ']' :
            if len(pars) == 0 :
                YorN += 1
                break
            elif pars[-1] == '(' :
                YorN += 1
                break
            elif pars[-1] == '[' :
                pars.pop()
    print('yes' if YorN == 0 and len(pars) == 0 else 'no')
# YorN 가 1 일경우와 남은 pars리스트의 길이가 0 초과일 경우 no 
            