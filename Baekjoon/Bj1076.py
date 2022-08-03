# 1076 저항 B2

import sys


sys.stdin = open('input.txt')

resis = {'black' : 0, 'brown' : 1, 'red' : 2, 'orange' : 3, 'yellow' : 4,
        'green' : 5, 'blue' : 6, 'violet' : 7, 'grey' : 8, 'white' : 9}

a = input()
b = input()
c = input()

ans = (resis[a]*10+resis[b])*(10**resis[c])
print(ans)