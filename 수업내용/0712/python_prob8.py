# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
# max() 함수 사용 금지

numbers = list(map(int, input().split()))

maxnum = numbers[0] #최댓값
max2num = numbers[0] #두 번째로 큰 값

for number in numbers :
    if maxnum < number :
        maxnum = number

for number in numbers :
    if number == maxnum :
        continue
    if max2num < number :
        max2num = number

print(max2num)