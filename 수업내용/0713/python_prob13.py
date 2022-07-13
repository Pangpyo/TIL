# 주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.

word = 'apple'

word_reverse = ''
for i in word :
    word_reverse = i + word_reverse
print(word_reverse)