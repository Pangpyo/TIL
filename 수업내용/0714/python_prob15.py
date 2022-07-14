# 문자열 word가 주어질 때, 해당 문자열에서 a 가 
# 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지

word = 'banana'
n = 0
a = 0
for i in word :
    n += 1
    if i == 'a' :
        a = n-1
        break
    a = -1
print(a)

word = 'HappyHacking'
n = 0
a = ''
for i in word :
    n += 1
    if i == 'a' :
        a += str(n-1)+' '
print(a)
        