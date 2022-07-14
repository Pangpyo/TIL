# 문자열 word가 주어질 때, Dictionary를 활용해서 
# 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.

word = 'banana'

for i in set(word) :
    n = 0
    for j in word :
        if i == j :
            n += 1
    if n > 0 :
        print(i, n)

n = 0
word_dic = {}
for i in word :
    word_dic_n = 0
    for j in word :
        if j == i :
            word_dic_n += 1
    word_dic[i] = word_dic_n

for key, value in word_dic.items():
    print(key, value)
