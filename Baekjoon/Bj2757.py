# 2757 엑셀 S3

import sys


def solution():
    input = sys.stdin.readline
    answer = []
    while True:
        r, c = input().rstrip().split('C')
        r = r[1::]
        c = int(c)
        if r == '0' and c == 0:
            break
        col = []
        
        while 1:
            c -= 1
            mod = c%26
            c //= 26
            col.append(chr(ord('A')+mod))
            if c == 0:
                break
        col.reverse()
        col.append(r)
        answer.append(''.join(col))
    return answer

if __name__ == "__main__":
    print(*solution(), sep='\n')