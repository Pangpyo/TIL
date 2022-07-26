# 2480 주사위 세개 B4

a, b, c = list(map(int, input().split()))
A = [a, b, c]
dice = [0 for i in range(6)] # 0이 6개 있는 리스트 생성

for i in A :
    dice[i-1] += 1 # 주사위 값의 출연 빈도를 각 자리에 저장

if max(dice) == 3 : # 중복되는 숫자의 최대개수를 세어줌
    print(10000 + (dice.index(max(dice))+1)*1000) #조건에 맞는 금액 출력
elif max(dice) == 2 :
    print(1000 + (dice.index(max(dice))+1)*100)
else :
    print(max(A)*100)