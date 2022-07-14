# 6066
# 3개의 정수(a, b, c)가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.

a, b, c = map(int, input().split())
list_a = [a, b, c]

for i in list_a :
    if i%2 == 0 :
        print('even')
    else :
        print('odd')

# 6067
# 0이 아닌 정수 1개가 입력되었을 때, 
# 음(-)/양(+)과 짝(even)/홀(odd)을 구분해 분류해보자.
# 음수이면서 짝수이면, A 음수이면서 홀수이면, B
# 양수이면서 짝수이면, C 양수이면서 홀수이면, D
# 를 출력한다.

n = int(input())
if n < 0 :
    if n%2 == 0:
        print('A')
    else :
        print('B')
else : 
    if n%2 == 0:
        print('C')
    else :
        print('D')

# 6068
# # 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.
# 평가 기준
# 점수 범위 : 평가
#  90 ~  100 : A
#  70 ~   89 : B
#  40 ~   69 : C
#  0  ~   39 : D
score = int(input())

if score >= 90 :
    print('A')
elif score >= 70 :
    print('B')
elif score >= 40 :
    print('C')
else :
    print('D')

# 6069
# 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

grade = input()

if grade == 'A' :
    print('best!!!')
elif grade == 'B' :
    print('good!!')
elif grade == 'C' :
    print('run!')
elif grade == 'D' :
    print('slowly~')
else :
    print('what?')

# 6070
# 월이 입력될 때 계절 이름이 출력되도록 해보자.

# 월 : 계절 이름
# 12, 1, 2 : winter
# 3, 4, 5 : spring
# 6, 7, 8 : summer
# 9, 10, 11 : fall

m = int(input())

if m//3 == 0 :
    print('winter')
elif m//3 == 1 :
    print('spring')
elif m//3 == 2 :
    print('summer')
elif m//3 == 3 :
    print('fall')