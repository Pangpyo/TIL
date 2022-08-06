# 1928 Base64 Decoder D2

import sys

sys.stdin = open('input.txt')

table = {}  # base64 테이블을 입력해줌.

for i in range(26) :
    table[chr(i+65)] = i

for i in range(26, 52) :
    table[chr(i+71)] = i
for i in range(52, 62) :
    table[str(i-52)] = i
table['+'] = 62
table['/'] = 63

T = int(input())
for x in range(1, T+1) :
    Encodedstr = input() # 인코딩된 문자열을 받음.
    
    bitpattern = '' # 인코딩된 문자열을 2진수로 바꾸어서 문자열로 저장해줄 변수
    for i in Encodedstr :
        index = table[i] # 인코딩된 문자열의 각 문자들을 
        for j in [5, 4, 3, 2, 1, 0] : 
            bitpattern += str(index//(2**j)) # 6자리의 2진수로 만들어 문자열로 저장해주었다.
            index = index%(2**j) 
    ans = ''
    while bitpattern : 
# bitpattern의 2진수들을 8개씩 받아 10진수로 바꾼 뒤,  아스키 코드에 맞는 문자를 찾아주었다.
        ans += chr(int(bitpattern[0:8], 2))
        bitpattern = bitpattern[8::]

    print('#%d'%x, ans)
