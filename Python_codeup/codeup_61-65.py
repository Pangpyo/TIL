# 6061
# 입력된 정수 두 개를 비트단위로 or 연산한 후 그 결과를 정수로 출력해보자.
# 비트단위(bitwise) 연산자 |(or, vertical bar, 버티컬바)를 사용하면 된다.

a, b = map(int, input().split())

print(a|b)

# 6062
# 입력된 정수 두 개를 비트단위로 xor 연산한 후 그 결과를 정수로 출력해보자.
# 비트단위(bitwise) 연산자 ^(xor, circumflex/caret, 서컴플렉스/카릿)를 사용하면 된다.

a, b = map(int, input().split())

print(a^b)

# 6063
# 입력된 두 정수(a, b) 중 큰 값을 출력하는 프로그램을 작성해보자.
# 단, 3항 연산을 사용한다.

a, b = map(int, input().split())
c = (a if (a>b) else b)
print(c)

# 6064
# 입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
# 단, 3항 연산을 사용한다.

a, b, c = map(int, input().split())
d = ((a if (a < b) else b) if ((a if (a < b) else b) < c) else c)
print(d)

# 6065
# 3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.

a, b, c = map(int, input().split())
list_a = [a, b, c]

for i in list_a :
    if i%2 == 0 :
        print(i)
