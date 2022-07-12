# 6036
# 단어와 반복 횟수를 입력받아 여러 번 출력해보자.

w, n = input().split()
print(w*int(n))

# 6037
# 반복 횟수와 문장을 입력받아 여러 번 출력해보자.

n = input()
s = input()
print(int(n)*s)

# 6038
# 정수 2개(a, b)를 입력받아
# a를 b번 곱한 거듭제곱을 출력하는 프로그램을 작성해보자.

a, b = list(map(int, input().split()))

print(a**b) #파이썬에서는 ^가 아닌 **사용

# 6039
# 실수 2개(f1, f2)를 입력받아
# f1을 f2번 거듭제곱한 값을 출력하는 프로그램을 작성해보자.

f1, f2 = list(map(float, input().split()))
print(f1**f2)

# 6040
# 정수 2개(a, b) 를 입력받아 a를 b로 나눈 몫을 출력해보자.

a, b = list(map(int, input().split()))

print(a//b) # 몫은 //를 사용