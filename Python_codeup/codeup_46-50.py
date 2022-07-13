# 6046
# 정수 1개를 입력받아 2배 곱해 출력해보자.

a = int(input())
print(a<<1) # <<n을 쓰면 값이 2^n배, >>n를 쓰면 값이 1/2^n배 된다

# 6047
# 정수 2개(a, b)를 입력받아 a를 2^b배 곱한 값으로 출력해보자.

a, b = map(int, input().split())
print(a<<b)

# 6048
# 두 정수(a, b)를 입력받아
# a가 b보다 작으면 True 를, a가 b보다 크거나 같으면 False 를 출력하는 프로그램을 작성해보자.

a, b = map(int, input().split())

print(a<b)

# 6049
# 두 정수(a, b)를 입력받아
# a와 b의 값이 같으면 True 를, 같지 않으면 False 를 출력하는 프로그램을 작성해보자.

a, b = map(int, input().split())

print(a==b)

# 6050
# 두 정수(a, b)를 입력받아
# b의 값이 a의 값 보다 크거나 같으면 True 를, 같지 않으면 False 를 출력하는 프로그램을 작성해보자.

a, b = map(int, input().split())

print(a<=b)