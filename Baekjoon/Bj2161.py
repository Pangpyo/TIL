# 2161 카드1 S5

from collections import deque


def solution() :
    card_1 = deque(range(1,int(input())+1))
    card_2 = []

    while 1 :
        card_2.append(card_1.popleft()) # 첫 인덱스에 있는 값 제거 후 새로운 리스트에 어펜드했다.
        if not card_1 : # card_1의 값이 모두 제거 된 경우 브레이크했다.
            break
        card_1.append(card_1.popleft()) # card_1의 첫 인덱스를 가장 뒤로 밀어 주었다.
    return card_2

if __name__ == "__main__" :
    print(*solution())