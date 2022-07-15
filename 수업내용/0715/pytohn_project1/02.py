f = open('data/fruits.txt', 'r')

berrys = ''
whatfruit = 'berry'
n = 0
while 1 :
    line = f.readline() 
    if whatfruit in line[len(line)-(len(whatfruit)+1):len(line)] :#끝이 berry로 끝나는 모든 줄들을 읽어옴
        if line not in berrys : #그 중 겹치지 않는 베리들만 berrys에 넣음
            berrys += line
            print(len(line))
            n += 1 #겹치지 않는 베리들의 갯수를 셈
    if not line : break
f.close() 

f = open('02.txt', 'w')
f.write('%d\n'%n)
f.write(berrys)
f.close()
print(n) 
print(berrys)

