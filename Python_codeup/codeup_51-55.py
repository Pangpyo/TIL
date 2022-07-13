# 6051
# 두 정수(a, b)를 입력받아
# a의 값이 b의 값과 서로 다르면 True 를, 같으면 False 를 출력하는 프로그램을 작성해보자.

a, b = map(int, input().split())

print(a!=b)

#6052
#정수가 입력되었을 때, True/False 로 평가해주는 프로그램을 작성해보자.
n = int(input())
print(bool(n))

#6053
#정수가 입력되었을 때, 그 불 값을 반대로 출력하는 프로그램을 작성해보자.

a = bool(int(input()))
print(not a)

# 6054
# 2개의 정수값이 입력될 때,
# 그 불 값이 모두 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.

a, b = input().split()
print(bool(int(a)) and bool(int(b)))

# 6055
# 2개의 정수값이 입력될 때,
# 그 불 값이 하나라도 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.

a, b = input().split()
print(bool(int(a)) or bool(int(b)))