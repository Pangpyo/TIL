# 1부터 n까지의 곱을 구하여 출력하는 코드를 
# 1) while 문 2) for 문으로 각각 작성하시오.

n = int(input())

i = 0
total = 1

while i < n : #while문 활용
    i += 1
    total = total*i
  
print(total)

#변수 초기화
total = 1


for i in range(n) : #for문 활용
    total = total*(i+1)
print(total)