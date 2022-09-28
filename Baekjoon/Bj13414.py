# 13414 수강신청 S3

import sys

input = sys.stdin.readline # 입력 줄 수가 많으므로 표준입력을 사용해야만 시간초과가 나지 않는다.
K, L = map(int, input().split()) 
dic = {}
for i in range(L):
    dic[input().rstrip()] = i 
    # 문자열로 입력을 받으므로 개행문자를 제거해주고, 학번 : 입력순으로 입력해준다. 같은 학번이 두번 이상 들어올 경우 늦게 들어온 값으로 순서값이 변한다.
dic = sorted(dic.items(), key=lambda x: x[1]) # 입력순서대로 정렬해준다.
for i in range(K): # dic에서 K개의 학번을 출력한다.
    if i >= len(dic): # 다만 K가 총 학번의 수보다 클 경우, 모든 학번을 출력하면 종료한다.
        break
    print(dic[i][0])
