#미세먼지 농도에 따른 등급 조건문

dust = int(input())

if dust > 150 :
    print('매우나쁨')
elif dust > 80 :
    print('나쁨')
elif dust > 30 :
    print('보통')
elif dust >= 0 :
    print('좋음')
else :
    print('0 이상을 입력하세요')