## 파이썬 제어문

* 파이썬은 기본적으로 위에서부터 아래로 순차적으로 명령을 수행 
* 특정 상황에 따라 코드를 선택적으로 실행(분기/조건)하거나 계속하여 실행(반복)하는 제어가 필요함 
* 제어문은 순서도(flow chart)로 표현이 가능

### 조건문

* 조건문은 참/거짓을 판단할 수 있는 조건식과 함께 사용

```python
#미세먼지 농도에 따른 등급 조건문

dust = int(input())

if dust > 150 :  # if : 조건문을 시작할때 
    print('매우나쁨')
elif dust > 80 : # elif : 복수의 조건을 걸 때 
    print('나쁨')
elif dust > 30 :
    print('보통')
elif dust >= 0 :
    print('좋음')
else : # 위의 조건을 제외한 나머지 경우에 대해
    print('0 이상을 입력하세요')
```

```python
if <expression>:
	# Code block
	if <expression>: # 조건문 안에서 복수의 조건을 쓸 때 사용하는 중첩 조건문. 들여쓰기에 주의
		# Code block
else:
# Code block
```

### 반복문

*  특정 조건을 도달할 때까지, 계속 반복되는 일련의 문장

```python
#wihle문

n = 0
total = 0
user_input = int(input())

while n <= user_input : # true, 1, a>0 등 다양한 조건을 넣을 수 있음
    total += n  
    n += 1 

print(total) 

```

```python
#for문
numbers = list(map(int, input().split()))

total = 0
length = 0
for number in numbers : # number가 numbers의 리스트를 0번째부터 순회
    total += number
    length += 1
print(total/length)

```

* 반복문 제어
  * break : 반복문 종료
  * continue : continue 이후의 코드블록을 수행하지 않고 다음 반복 수행
  * for-else : 끝까지 반복문을 실행한 이후에 else문 실행(break되면 수행하지 않음)