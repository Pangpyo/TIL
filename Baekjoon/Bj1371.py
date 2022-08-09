# 1371 가장 많은 글자 B2

import sys


sys.stdin = open('input.txt')

text = sys.stdin.read()

dic = {}
for i in text :
    if i == ' ' or i == '\n' : # 공백과 줄바꿈을 세지 않아야하므로 continue한다.
        continue
    if i not in dic :
        dic[i] = 1 # 딕셔너리에 없는 알파벳일 경우 추가
    else : # 있을 경우 벨류에 +1
        dic[i] += 1

ans = sorted([i for i, v in dic.items() if v == max(dic.values())]) 
# 벨류가 가장 큰 알파벳들 저장 후 사전 순으로 정렬

print(*ans, sep='') # 띄어쓰기 없이 출력