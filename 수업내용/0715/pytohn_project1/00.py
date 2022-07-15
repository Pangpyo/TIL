f = open("00.txt", 'w')

f.write('2회차 김광표 \nHello, Python!\n')

for i in range(1,6) :
    data = '%d일차 파이썬dd 공부 중\n' %i
    f.write(data)
f.close()
