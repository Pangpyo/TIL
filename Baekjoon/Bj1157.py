# 1157 단어공부 B1

word = input().upper() 
# 문제에서는 대소문자를 구분하지 않고 가장 많이 입력된 알파벳을 찾아야한다.
# 또한 출력값은 전부 대문자로 해야하므로 입력받은 문자열을 대문자로 바꿔준다.
word_count = {}
for i in word : # word의 각 인덱스를 검사해 알파벳 : 개수의 딕셔너리를 만들어주었다.
    if i not in word_count :
        word_count[i] = 1
    elif i in word_count :
        word_count[i] += 1
max_word = [i for i,v in word_count.items() if max(word_count.values()) == v]
# 가장 많은 개수를 가진 알파벳의 모음을 만들었다.
if len(max_word) == 1 : # 알파벳의 개수를 세어 1개면 해당 알파벳 출력, 2개 이상이면 ?를 출력했다
    print(max_word[0]) # max_word는 리스트이므로 첫번째 항을 출력해 문자열만 출력했다.
else :
    print('?')