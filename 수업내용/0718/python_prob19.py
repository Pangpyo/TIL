# 문제 19. 숫자의 길이 구하기
# 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
# 양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지

def lenth_n(number) :
    lenth = 1
    while 1 :
        if number/10 >= 1 :
            number = number/10
            lenth += 1
        else :
            break
    return lenth

number = int(input())
print(lenth_n(number))