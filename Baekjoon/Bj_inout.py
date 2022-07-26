# 1. 1000. A+B B5

from curses import BUTTON5_TRIPLE_CLICKED
from termios import B50


A, B = map(int, input().split())

print(A+B)

# 2. 2558 A+B 2 B5

A = int(input())
B = int(input())

print(A+B)

# 3. 10950 A+B 3 B5

T = int(input())

for i in range(1, T+1) :
    A, B = map(int, input().split())
    print(A+B)

# 4. 10953 A+B 6 B2

T = int(input())

for i in range(1, T+1) :
    A, B = map(int, input().split(','))
    print(A+B)

# 5. 11021 A+B 7 B5

T = int(input())

for i in range(1, T+1) :
    A, B = map(int, input().split())
    print('Case #%d:'%i,A+B)

# 6. 11022 A+B 8 B5

T = int(input())

for i in range(1, T+1) :
    A, B = map(int, input().split())
    print(f'Case #{i}: {A} + {B} = {A+B}')

# 7. 10952 A+B 5 B5

while 1 :
    A, B = map(int, input().split())
    if A == 0 and B == 0 :
        break
    print(A+B)

# 8. 2438 별 찍기 - 1 B5

N = int(input())

for i in range(1, N+1) :
    print('*'*i)

# 9. 2439 별 찍기 - 2 B4

N = int(input())

for i in range(1, N+1) :
    print(' '*(N-i),'*'*i, sep='')

# 10. 10995 별 찍기 - 20 B3

N = int(input())

a = 1
for i in range(1, N+1) :
    s = '* '
    print(s[::a]*N)
    a *= -1

# 11. 1330 두 수 비교하기 B5

A, B = map(int,input().split())

if A > B :
    print('>')
elif A < B :
    print('<')
else :
    print('==')

# 12. 9498 시험 성적 B5

N = int(input())

if N >= 90 : print('A')
elif N >= 80 : print('B')
elif N >= 70 : print('C')
elif N >= 60 : print('D')
else : print('F')

# 13. 2753 윤년 B5

N = int(input())

if N%4 == 0 and N%100 != 0 :
    print(1)
elif N%400 == 0 :
    print(1)
else : 
    print(0)

# 14. 14681 사분면 고르기 B5

x = int(input())
y = int(input())

if x > 0 and y > 0 : print(1)
elif x < 0 and y > 0 : print(2)
elif x < 0 and y < 0 : print(3)
else : print(4)

# 15. 2739 구구단 B5

N = int(input())

for i in range(1, 10) :
    print(f'{N} * {i} = {N*i}')

# 16. 8393 합 B5

N = int(input())
print(sum(list(range(1, N+1))))

# 17. 2741 N찍기 B5

N = int(input())
for i in range(1, 1+N) : print(i)

# 18. 2742 기찍N B4

N = int(input())
A = list(range(1, 1+N))
for i in A[::-1] : print(i)