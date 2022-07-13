# 주어진 리스트 numbers에서 최댓값을 구하여 출력하시오.
# max() 함수 사용 금지

# numbers = [0, 20, 100]
numbers = list(map(int, input().split()))

maxnum = numbers[0]

for number in numbers :
    if maxnum < number :
        maxnum = number
print(maxnum)