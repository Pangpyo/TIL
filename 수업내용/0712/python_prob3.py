# 1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.

# sum() 함수 사용 금지

n = int(input())


i = 0
total = 0

while i <= n : #while문 활용
    total += i
    i += 1
print(total)

i = 0 #변수 초기화
total = 0


for i in range(n+1) : #for문 활용
    total += i
print(total)
