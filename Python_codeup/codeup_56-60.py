# 6056
# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 서로 다를 때에만 True 를 출력하는 프로그램을 작성해보자.



a, b = map(bool, map(int, input().split()))

print((a and (not b)) or ((not a) and b))

# 6057
# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 서로 같을 때에만 True 를 출력하는 프로그램을 작성해보자.

a, b = map(bool, map(int, input().split()))

print(a and b or (not a)and (not b))

# 6058
# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 모두 False 일 때에만 True 를 출력하는 프로그램을 작성해보자.

a, b = map(bool, map(int, input().split()))

print(not(a or b))

# 5059
# 입력 된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력해보자.
# 비트단위(bitwise)연산자 ~ 를 붙이면 된다.(~ : tilde, 틸드라고 읽는다.)

a = int(input())

print(~a) #'~'를 사용하면 변수를 2진법 기준으로 반전 할 수 있다.

# 5060
# 입력된 정수 두 개를 비트단위로 and 연산한 후 그 결과를 정수로 출력해보자.
# 비트단위(bitwise)연산자 &를 사용하면 된다.

a, b = map(int, input().split())

print(a&b) #'&'를 사용해 두 비트열중 둘 다 1인부분만 출력한다