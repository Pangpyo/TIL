# 6084
# 소리 파일 저장용량 계산하기


from re import I


s, h, b, c = map(int, input().split())

mb = s*h*b*c/8/1024/1024

print('%.1f'%mb, 'MB')

# 6085
# 그림 파일 저장용량 계산하기

w, h, b = map(int, input().split())

px = (w*h*b)/8/1024/1024

print('%.2f'%px, 'MB')

# 6086
# 거기까지! 이제 그만~

n = int(input())
i = 0
total = 0
while 1 :
    i += 1
    total += i
    if total >= n :
        break
print(total)

# 6087
# 3의 배수는 통과

n = int(input())
for i in range(1,n+1) :
    if i%3==0 :
        continue
    print(i, end=' ')

# 6088
# 수 나열하기

a, d, n = map(int, input().split())

print(a+d*(n-1))

# 6089
# 수 나열하기2

a, d, n = map(int, input().split())

print(a*d**(n-1)-1)

# 6090
# 수 나열하기3

a, m, d, n = map(int, input().split())


for i in range(1,n) :
    a = a*m+d
print(a)