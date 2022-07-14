# 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
# .upper(), .swapcase() 사용 금지

word = input('소문자 단어를 입력하세요 : ')
word_upper = ''
for i in word :
    word_upper += chr(ord(i)-32)
print('대문자로 변환되었습니다  :',word_upper)