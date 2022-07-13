# 6041
# 정수 2개(a, b) 를 입력받아 a를 b로 나눈 나머지를 출력해보자.

a, b = map(int, input().split())

print(a%b)

# 6042
# 실수 1개를 입력받아
# 소숫점 이하 두 번째 자리까지의 정확도로 반올림한 값을 출력해보자.

a=input()
a=float(a)
print( format(a, ".2f") )

# 6043
# 실수 2개(f1, f2)를 입력받아 f1 을 f2 로 나눈 값을 출력해보자. 
# 이 때 소숫점 넷째자리에서 반올림하여 무조건 소숫점 셋째 자리까지 출력한다.

f1, f2=map(float,input().split())

print( format(f1/f2, ".3f") )

# 6044
# 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
# 단, b는 0이 아니다.

a, b = map(int,input().split())

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format(a/b, ".2f"))

# 6045
# 정수 3개를 입력받아 합과 평균을 출력해보자.

a, b, c = map(int, input().split())
s = a+b+c
print(s, format(s/3, ".2f"))