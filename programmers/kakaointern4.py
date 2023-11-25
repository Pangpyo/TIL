def solution(coin, cards):
    answer = 1
    n = len(cards)
    my_cards = []
    have = 0
    def is_need(cards, ncard) : # 특정 카드뭉치와 합쳐 n+1이 나오는 카드인지 판단
        flag = False
        idx = 0
        for i, card in enumerate(cards) :
            if card + ncard == n+1 :
                flag = True
                idx = i
                break
        if flag : # 그런 경우 합칠 카드 pop후 True 리턴
            cards.pop(idx)
            return True
        return False
    for i in range(n//3) : # n//3만큼을 합칠카드를 판단하면서 가져오기
        flag = is_need(my_cards, cards[i])
        if flag :
            have += 1
        else :
            my_cards.append(cards[i])
    trash_cards = [] # 버릴카드들 
    trash_have = 0 # 버린카드중 바로 n+1이 되는 것의 개수
    for i in range(n//3, n, 2) :
        for j in range(2) :
            if coin and is_need(my_cards, cards[i+j]) : # coin 1개이상 있고, 내 카드와 합칠 수 있는경우
                coin -= 1
                have += 1
            elif coin >= 2 and is_need(trash_cards, cards[i+j]) : # 코인이 2개 이상 있고, 버린카드중 합칠 수 있는경우
                trash_have += 1
            else : # 이 외의 경우엔 버리기
                trash_cards.append(cards[i+j])
        have -= 1 # n+1 하나 없애기
        if have < 0 :
            if coin >= 2 and trash_have : # 만약 당장 내 카드안에서 해결이 불가능한 경우, 버린카드중에서라도 가져오기
                coin -= 2
                trash_have -= 1
                have += 1
            else :
                break
        answer += 1
    return answer

coin = 2
cards = [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7]
print(solution(coin, cards))