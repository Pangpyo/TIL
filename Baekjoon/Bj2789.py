# 2789 유학금지 B2

delete = 'CAMBRIDGE'

word = input()

for i in delete :
    if i in word :
        word = word.replace(i,"")

print(word)