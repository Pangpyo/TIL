from itertools import product

def solution(users, emoticons):
    m = len(emoticons)
    sales = list(product([10, 20, 30, 40], repeat=m))
    print(sales)
    answer = []
    return answer

users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]

solution(users, emoticons)
