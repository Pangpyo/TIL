from itertools import product

def solution(users, emoticons):
    m = len(emoticons) # 이모티콘의 개수
    sales = list(product([10, 20, 30, 40], repeat=m)) # 품목별 할인율의 모든 경우의 수
    answer = []
    maxeplus = 0 # 이모티콘 플러스를 가장 많이 가입한 경우
    for sale in sales :
        info = [0, 0] # [가입수, 구매금액]
        for user in users : # 각 유저별
            want, money = user # 원하는 할인율과 구매할 금액
            price = 0 # 구매 가능 금액
            e_plus = False # 이모티콘 플러스 가입 여부
            for i in range(m) :
                if sale[i] >= want : # 해당 이모티콘의 할인율이 원하는 할인율을 넘어가면
                    price += int(emoticons[i]*((100-sale[i])/100)) # 할인 된 가격으로 구매한다.
            if price >= money : # 만약 총 구매 금액이 구매 가능 금액 이상일 경우
                e_plus = True # 이모티콘 플러스를 가입한다.
            if e_plus : # 이모티콘 플러스를 가입 한 경우
                info[0] += 1 # 이모티콘 플러스 가입자 수 + 1
            else : # 가입하지 않은 경우
                info[1] += price # 총 구매 금액 +

        if info[0] >= maxeplus : # 이모티콘 플러스 가입자 수가 이전까지의 가입자 수보다 많거나 같을 경우
            print(sale, info) 
            answer.append(info) # 해당 정보를 답에 더해준다.
            maxeplus = info[0] # 이모티콘 플러스 가입자 수 최신화
    answer.sort(reverse=True) # 가입자수, 구매 금액 역순으로 정렬
    print(answer)
    return answer[0]