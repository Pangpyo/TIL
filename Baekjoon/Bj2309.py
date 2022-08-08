# 2309 일곱 난쟁이 B1

import sys


sys.stdin = open('input.txt')

dwarf = []

for _ in range(9) :
    dwarf.append(int(input())) # 난쟁이들을 리스트로 받음
dwarf.sort() # 내림차순 정렬
total9 = sum(dwarf) # 9난쟁이들의 키의 총 합
for i in range(8) :
    for j in range(i+1, 9) :
        a = dwarf[i] # 난쟁이들을 둘씩 뽑아 키의 총 합에서 두 난쟁이의 키의 합을 뺀 값이
        b = dwarf[j] # 100이 되는지 확인
        if total9 - a - b == 100 :
            dwarf.remove(a) # 해당하는 난쟁이들을 리스트에서 지움
            dwarf.remove(b)
            print(*dwarf, sep='\n')
            exit(0)
