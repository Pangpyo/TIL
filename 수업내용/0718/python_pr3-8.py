# 예제 03. [오류 해결] 입력 받기
# 오류 코드
# numbers = input().split()
# print(sum(numbers))

numbers = map(int, input().split()) # map을 통해 받은 코드들을 모두 정수로 받는다.
print(sum(numbers))

# 예제 04. [오류 해결] 입력 받기 - 2
# 오류 코드
# words = list(map(int, input().split()))
# print(words)

words = list(map(str, input().split())) #문자열이므로 int>str
print(words)

# 예제 05. [오류 해결] 숫자의 길이 구하기
# 오류 코드
# number = 22020718
# print(len(number))

number = 22020718
print(len(str(number))) #숫자의 길이를 구하려면 문자열로 바꿔주어야 한다.

# 예제 06. [오류 해결] 1부터 N까지의 2의 곱 저장하기
# 오류 코드
# N = 10
# answer = ()
# for number in range(N + 1):
#     answer.append(number * 2)

# print(answer)
N = 10

answer = [] #리스트로 저장해야하므로 소괄호가 아닌 대괄호가 들어간다.
for number in range(1, N + 1): #문제에서 1부터 N까지라고 했으므로 (1,N+1)의 범위가 맞는것같다.
    answer.append(number * 2)

print(answer)

# 예제 07. [오류 해결] 평균 구하기
# 오류코드
# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# total = 0
# count = 0

# for number in number_list:
#     total += number
# count += 1

# print(total // count)

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1 #들여쓰기를 해 for문 안에서 카운트가 늘어나게 해야한다.

print(total/count) #평균을 구하는 것이므로 몫을 구하는 것이 아닌 나눗셈을 해야한다.

# 예제 08. [오류 해결] 모음의 개수 찾기
# 오류 코드
# word = "HappyHacking"

# count = 0

# for char in word:
#     if char == "a" or "e" or "i" or "o" or "u":
#         count += 1

# print(count)

word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u": #매 문자마다 조건을 써야한다.
        count += 1

print(count)
