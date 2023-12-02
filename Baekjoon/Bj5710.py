# 5710 전기요금 G4
import sys


def solution() :
    answers = []
    input = sys.stdin.readline
    def get_price(use) :
        if use > 1000000 :
            return use*7 - 2020100
        elif use > 10000 :
            return use*5 - 20100
        elif use > 100 :
            return use*3 - 100
        else :
            return use*2
    def get_use(price) :
        if price > 4979900 :
            return (price + 2020100)//7
        elif price > 29900 :
            return (price + 20100)//5
        elif price > 200 :
            return (price + 100)//3
        else :
            return price//2
    while True :
        A, B = map(int, input().split())
        if A == B == 0 :
            break
        answer = 0
        total = get_use(A)
        s = 0
        e = total//2
        while s <= e :
            m = (s+e)//2
            price = get_price(m)
            you = total - m
            you_price = get_price(you)
            diff = you_price - price
            if diff < B :
                e = m - 1
            elif diff == B :
                answer = price
                break
            else :
                s = m + 1
        answers.append(answer)
    return answers

if __name__ == "__main__" :
    print(*solution(), sep='\n')