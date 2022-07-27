# 2941 크로아티아 알파벳 S5

cro_alpabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] # 크로아티아 알파벳 지정

word = input()

for i in cro_alpabet : # 각 크로아티아 알파벳을 검사
    if i in word : 
        word = word.replace(i,"z") #크로아티아 알파벳이 있을시 z라는 임의의 알파벳으로 바꿔줌

print(len(word)) # 문자열 길이 출력