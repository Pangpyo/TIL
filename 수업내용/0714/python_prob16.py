# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u 
# count() 사용 금지

vowel = ['a', 'e', 'i', 'o', 'u']

word = input()
n = 0
for i in word :
    for j in vowel :
        if j == i :
            n += 1
print(n)