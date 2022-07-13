# 6031
# 10진 정수 1개를 입력받아
# 유니코드 문자로 출력해보자.

c = int(input())
print(chr(c))

# 6032
# 입력된 정수의 부호를 바꿔 출력해보자.

a = int(input())
print(-a)

# 6033
# 문자 1개를 입력받아 그 다음 문자를 출력해보자.

a = ord(input())
print(chr(a+1))

# 6034
# 정수 2개(a, b)를 입력받아 a에서 b를 뺀 차를 출력하는 프로그램을 작성해보자.

a, b = list(map(int, input().split()))
print(a-b)

# 6035
# 실수 2개(f1, f2)를 입력받아 곱을 출력하는 프로그램을 작성해보자.

f1, f2 = list(map(float, input().split()))
print(f1*f2)