#6016
#공백을 두고 문자(character) 2개를 입력받아 순서를 바꿔 출력해보자

c1, c2 = input().split()
print(c2, c1)

#6017
#정수(integer), 실수, 문자(character), 문자열(string) 등 1개만 입력받아 한 줄로 3번 출력해보자

s = input()
print(s, s, s)

#6018
#24시간 시:분 형식으로 시간이 입력될 때, 그대로 출력하는 연습을 해보자

h, m = input().split(':')
print(h, m, sep=':')

#6019
#"연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자

y, m, d = input().split('.')
print(d, m, y, sep='-')

#6020
#주민번호는 다음과 같이 구성된다.
#XXXXXX-XXXXXXX
#왼쪽 6자리는 생년월일(YYMMDD)이고, 오른쪽 7자리는 성별,출생지역,확인코드로 구성되어있다.
#주민번호를 입력받아 형태를 바꿔 출력해보자.

a, b = input().split('-')
print(a, b, sep='')