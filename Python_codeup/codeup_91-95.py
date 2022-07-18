# 6091 : [기초-종합] 함께 문제 푸는 날(설명)

a, b, c = map(int, input().split())
d = 1
while 1 :
    if d%a ==0 and d%b ==0 and d%c ==0 :
        break
    d +=1
print(d)

# 6092 : [기초-리스트] 이상한 출석 번호 부르기1

n = int(input())
a = list(map(int, input().split()))

d = []
for i in range(0,23) : 
    d.append(0)

for i in range(n) :
    d[a[i]-1] += 1

for i in d :
    print(i, end=' ')

# 6093 : [기초-리스트] 이상한 출석 번호 부르기2

n = int(input())
a = list(map(int, input().split()))

for i in range(n) :
    print(a[n-i-1], end=' ') 

# 6094 : [기초-리스트] 이상한 출석 번호 부르기3

n = int(input())
a = list(map(int, input().split()))

# 6095 : [기초-리스트] 바둑판에 흰 돌 놓기

n = int(input())
d = []
for i in range(19) :
    d.append([])
    for j in range(19) :
        d[i].append(0)


for i in range(n) :
    x,y = map(int, input().split())
    d[x-1][y-1] = 1

for i in range(19) :
    for j in range(19) :
        print(d[i][j], end=" ")
    print('')


