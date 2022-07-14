# 6076
# 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.

c = int(input())

for i in range(0, c+1) :
    print(i)

# 6077
# 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.

c = int(input())
n = 0
for i in range(0, c+1) :
    if i%2 == 0 :
        n += i
print(n)

# 6078
# 영문 소문자 'q'가 입력될 때까지
# 입력한 문자를 계속 출력하는 프로그램을 작성해보자.

while 1 :
    c = input()
    print(c)
    if c == 'q' :
        break

# 6079
# 1, 2, 3 ... 을 계속 더해 나갈 때,
# 그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만
# 계속 더하는 프로그램을 작성해보자.

n = int(input())
i = 0
s = 0
while 1 :
    i += 1
    s += i
    if s >= n :
        print(i)
        break

# 6080
# 1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때,
# 나올 수 있는 모든 경우를 출력해보자.

n, m = map(int, input().split())

for i in range(1, 1+n) :
    for j in range(1, 1+m) :
        print(i,j)