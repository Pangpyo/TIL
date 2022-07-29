# 7785 회사에 있는 사람 S5

import sys

sys.stdin = open("input.txt")

n = int(input())
access_record = []
for i in range(n) :
    acc = tuple(input().split())
    if acc[1] == 'enter' :
        access_record.append(acc[0]) # 출근했을 때 리스트에 이름을 더해줌
    else :
        access_record.remove(acc[0]) # 퇴근시 리스트에성 이름을 제거해줌

access_record.sort(reverse = True) # 사전 역순으로 정렬

print(*access_record, sep= '\n') # 리스트를 한 줄씩 띄어서 출력