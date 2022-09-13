# 1599 민식어 S1

import sys


sys.stdin = open('input.txt')

listm = ['a', 'b', 'k', 'd', 'e', 'g', 'h', 'i', 'l', 'm', 'n', 'ng', 'o', 'p', 'r', 's', 't', 'u', 'w', 'y'] # 민식어의 순서를 찾기 위한 리스트

N = int(input())

words = [] # 단어를 입력받음
dic = {} # 민식어 : 대응하는 영단어로 딕셔너리를 만듦
for i in range(N) :
    word = input()
    mtoe = [] # 민식어 to 대응 영어로 바꿔줄 행렬
    for w in range(len(word)) :

        if word[w] =='g' and mtoe and word[w-1] == 'n': # g가 나왔는데, 이전 알파벳이 n 이면
            mtoe.pop() # n을 지워주고
            mtoe.append(chr(97+listm.index('ng'))) # ng에 대응하는 알파벳을 넣어준다
        else :
            mtoe.append(chr(97+listm.index(word[w]))) # 민식어에 대응하는 영어 알파벳을 넣어준다
    dic[word] = ''.join(mtoe) # 해당 단어를 문자열로 만들어 딕셔너리에 대응시킨다.
dic = sorted(dic.items(), key = lambda x : x[1]) # 대응하는 알파벳 순서로 정렬
for m, a in dic :
    print(m) # 정렬한 단어를 출력


