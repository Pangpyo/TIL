# 6071
# 임의의 정수가 줄을 바꿔 계속 입력된다.
# -2147483648 ~ +2147483647, 단 개수는 알 수 없다.

# 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.

while 1 :
    n = int(input())
    if n == 0 :
        break
    print(n)

# 6072
# 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

n = int(input())
while 1 : 
    print(n)
    n -= 1
    if n == 0 :
        break

# 6073
# 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

n = int(input())
while 1 : 
    n -= 1
    if n == 0 :
        break
    print(n)

# 6074
# 영문 소문자(a ~ z) 1개가 입력되었을 때,
# a부터 그 문자까지의 알파벳을 순서대로 출력해보자.

c = ord(input())
a = ord('a')
s = ''
for i in range(a, c+1) :
    s += chr(i)+' '
print(s)

# 6075
# 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.

c = int(input())

for i in range(0, c+1) :
    print(i)