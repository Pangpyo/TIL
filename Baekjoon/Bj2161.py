# 2161 카드1 S5

from collections import deque

N = int(input())

card_1 = deque(range(1,N+1))

card_2 = []

while 1 :
    a = card_1.popleft() # 첫 인덱스 제거 후 새로운 리스트에 어펜드했다.
    card_2.append(a)
    if not card_1 : # card_1의 인덱스가 모두 제거 된 경우 브레이크했다.
        break
    b = card_1.popleft() # card_1의 첫 인덱스를 가장 뒤로 밀어 주었다.
    card_1.append(b)
    
print(*card_2)