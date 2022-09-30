# 2021 Dev-Matching: 웹 백엔드 개발자(상반기) 다단계 칫솔 판매


def solution(enroll, referral, seller, amount):
    N = len(enroll)
    dic_enroll = {}
    dic_seller = {}
    result = [0] * N
    for i in range(N):
        dic_enroll[enroll[i]] = i
    for i in range(len(seller)):
        dic_seller[seller[i]] = amount[i]
    for i in range(N):
        sun = enroll[i]
        if sun not in seller:
            continue
        money_sun = dic_seller[sun] * 100
        while 1:
            parent = referral[dic_enroll[sun]]
            money_parent = money_sun // 10
            money_sun -= money_parent
            result[dic_enroll[sun]] += money_sun
            if not money_parent:
                break
            if parent == "-":
                break
            sun = parent
            money_sun = money_parent

    return result


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

print(solution(enroll, referral, seller, amount))
