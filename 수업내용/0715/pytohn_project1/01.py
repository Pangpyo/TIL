f = open('data/fruits.txt', 'r')

n = 0
while 1 :
    line = f.readline()
    if not line : break
    n += 1
f.close()

f = open('01.txt', 'w')
f.write('%d'%n)
f.close()
print(n)