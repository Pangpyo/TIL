# 주어진 숫자의 평균을 구하는 코드를 작성하시오.
# sum(), len()  함수 사용 금지

numbers = list(map(int, input().split()))

total = 0
length = 0
for number in numbers :
    total += number
    length += 1
print(total/length)

