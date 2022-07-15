# 6081
# 16진수(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F)를 배운
# 영일이는 16진수끼리 곱하는 16진수 구구단?에 대해서 궁금해졌다.

# A, B, C, D, E, F 중 하나가 입력될 때,
# 1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자.
# (단, A ~ F 까지만 입력된다.)

h = int(input(),16)

for i in range(1,16) : 
    print('%X'%h, '*%X'%i,'=%X'%(h*i), sep='')

# 6082
# 친구들과 함께 3 6 9 게임을 하던 영일이는 잦은 실수 때문에 계속해서 벌칙을 받게 되었다.
# 3 6 9 게임의 왕이 되기 위한 369 마스터 프로그램을 작성해 보자.

n = int(input())
a = ''
for i in range(1,n+1) :
    if (i%10) == 0 :
        a += str(i)+' '
    elif (i%10)%3 == 0 :
        a += 'X'+' '
    else :
        a += str(i)+' '
print(a)

# 6083
# 빨강(red), 초록(green), 파랑(blue) 빛을 섞어 여러 가지 다른 색 빛을 만들어 내려고 한다.

# 빨강(r), 초록(g), 파랑(b) 각 빛의 가짓수가 주어질 때,
# 주어진 rgb 빛들을 섞어 만들 수 있는 모든 경우의 조합(r g b)과 만들 수 있는 색의 가짓 수를 계산해보자.  

r, g, b = map(int, input().split())
n = 0
for i in range(0,r) :
    for j in range(0,g) :
        for k in range(0,b) :
            print(i, j, k)
            n += 1
print(n)