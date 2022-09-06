# 10814 나이순 정렬 S5

import sys
input = sys.stdin.readline
peaple = []
for i in range(int(input())) :
    age, name = input().split()
    peaple.append((int(age), name, i))
peaple = sorted(peaple, key=lambda x : (x[0], x[2]))
for p in peaple :
    print(p[0], p[1])
