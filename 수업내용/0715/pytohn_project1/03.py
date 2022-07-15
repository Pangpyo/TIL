import pprint
f = open('data/fruits.txt', 'r')

fruits = {}
n = 0
while 1 :
    line = f.readline()
    line = line.strip('\n')
    if not line : break
    if not line in fruits :
        fruits[line] = 1
    else :
        fruits[line] = fruits[line] +1

f.close() 

with open('03.txt','w', encoding='UTF=8') as f :
    for fruit, n in fruits.items() :
       f.write(f'{fruit} : {n}\n')

pprint.pprint(fruits)
