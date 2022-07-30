# 2027. 대각선 출력하기 D1

n = int(input())

for i in range(n) :
    a = '+'*i + '#' + '+'*(n-i-1)
    print(a)
