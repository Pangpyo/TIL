# 2864 5와 6의 차이 B2

a, b = input().split()

def fivesix(str) :
    maxans = str
    if '5' in str :
        maxans = str.replace('5','6')
    minans = str
    if '6 in str' :
        minans = str.replace('6','5')
    return int(minans), int(maxans)

a5 , a6 = fivesix(a)
b5, b6 = fivesix(b)
print(a5 + b5, a6 + b6)