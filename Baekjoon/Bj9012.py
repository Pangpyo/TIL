# 9012 괄호 S4

from collections import deque
import sys

sys.stdin = open('19_괄호.txt')

T = int(input())

for i in range(T) :
    PS = list(input().rstrip()) # 문자열을 리스트로 받았다.
    for _ in range(len(PS)) : 
        if PS[0] == '(' : # '('가 나오면 제거했다.
            PS.pop(0)
            if ')' in PS : 
# '('를 제거 한 뒤 ')'도 제거해주었고, '('와 함께 제거할 ')' 가 없는 경우 NO 출력 후 브레이크했다.
                PS.remove(')')
            else : 
                print('NO')
                break
        else : # 리스트의의 시작이 '(' 가 아닌 경우에도 NO 출력 후 브레이크했다.
            print('NO')
            break
        if not PS : # 리스트를 모두 제거한 경우 YES를 출력해주었다.
            print('YES')
            break
