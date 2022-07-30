# 10804. 문자열의 거울상 D3
import sys

sys.stdin = open("_문자열의거울상.txt")

T = int(input())

for i in range(1, T+1) :
    bdpq = input()
    pqbd = '' # 새로 만든 문자열이 들어갈 변수를 만들었다.
    for j in range(len(bdpq)) : # 입력받은 단어의 인덱스를 검사했다. 
        if bdpq[j] == 'b' :  # 각 알파벳에 대응되는 알파벳을 새로운 문자열에 더해주었다.
            pqbd += 'd'
        elif bdpq[j] == 'd' :
            pqbd += 'b' 
        elif bdpq[j] == 'p' :
            pqbd += 'q'
        else :
            pqbd += 'p'
    print('#%d'%i, pqbd[::-1]) # 슬라이싱해 출력했다.
