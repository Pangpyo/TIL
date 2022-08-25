# 2527 직사각형 S1

import sys


sys.stdin = open('input.txt')

for _ in range(4) :
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    
    if q1 < y2 or q2 < y1 or x1 > p2 or p1 < x2 :
        print('d')
    elif p1 == x2 :
        print('c' if (q1 == y2 or y1 == q2) else 'b')
    elif x1 == p2 :
        print('c' if (q1 == y2 or y1 == q2) else 'b')
    elif q1 == y2 :
        print('c' if (p1 == x2 or x1 == p2) else 'b')
    elif y1 == q2 :
        print('c' if (p1 == x2 or x1 == p2) else 'b')
    else :
        print('a')