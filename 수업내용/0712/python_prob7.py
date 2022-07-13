# 주어진 리스트 numbers에서 최솟값을 구하여 출력하시오.
# min() 함수 사용 금지

numbers = numbers = list(map(int, input().split()))

minnum = numbers[0]

for number in numbers :
    if minnum > number :
        minnum = number

print(minnum)