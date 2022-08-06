# 2056 연월일 달력 D1

import sys


sys.stdin = open('input.txt')


T = int(input())

def calender(i, ymd) :
    day31 = [1, 3, 5, 7, 8, 10, 12]
    day30 = [4, 6, 9, 11]
    day28 = [2]
    year = ymd[0:4]
    month = ymd[4:6]
    day = ymd[6:8]
    if int(month) in day31 :
        if int(day) > 31 :
            return -1
    elif int(month) in day30 :
        if int(day) > 30 :
            return -1
    elif int(month) in day28 :
        if int(day) > 28 :
            return -1
    else :
        return -1
    month = str(month)
    return year+'/'+month+'/'+day

for i in range(1, T+1) :
    ans = calender(i, input())
    print('#%d'%i, ans)