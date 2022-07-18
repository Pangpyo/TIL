# 예제 09. [오류 해결] 과일 개수 구하기
from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        # fruit_count = {fruit: 1} 오류코드
        fruit_count[fruit] = 1 #딕셔너리의 키를 지정 해서 값을 넣어줘야한다.
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)

# 예제 10. [오류 해결] 더 큰 최댓값 찾기

number_list = [1, 23, 9, 6, 91, 59, 29]
# max = max(number_list) 오류코드
max1 = max(number_list) 
#max는 함수 이름인데, max를 변수로 사용하면 아래에서 max가 함수가 아닌 변수로만 사용되니 변수 이름을 바꿔줘야한다.
#이하의 max변수들도 모두 max1로 바꿔주었다.
number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max2 = max(number_list2)

if max1 > max2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif max1 < max2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")

