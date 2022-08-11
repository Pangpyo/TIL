# 6996 애너그램 B1

import sys


sys.stdin = open('input.txt')

for _ in range(int(input())) :
    ans = ''
    A, B = input().split()
    if sorted(A) != sorted(B) :
        ans = 'NOT '
    print(f'{A} & {B} are {ans}anagrams.')
