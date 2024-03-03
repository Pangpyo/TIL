# 18119 단어 암기 G4

from collections import defaultdict
import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())

    chars = (1<<21)-1
    know = defaultdict(int)
    forgets = defaultdict(int)
    know_set = set()
    forgets_set = set()

    cnt = 0
    dic = {}
    vowel = ('a', 'e', 'i', 'o', 'u')
    total = N
    for i in range(ord('a'), ord('z')+1) :
        if chr(i) in vowel :
            continue
        dic[chr(i)] = cnt
        cnt += 1
    for _ in range(N) :
        word = input().rstrip()
        bit = 0
        for w in word :
            if w in vowel :
                continue
            bit |= 1<<dic[w]
        know_set.add(bit)
        know[bit] += 1
    answer = []
    for _ in range(M) :
        o, x = input().split()
        temp = []
        if x in vowel :
            if answer :
                answer.append(answer[-1])
            else :
                answer.append(N)
            continue
        if o == '2' :
            chars |= 1<<dic[x]
            for w in forgets_set :
                if chars | w == chars :
                    temp.append(w)
            for w in temp :
                know[w] = forgets[w] 
                forgets[w] = 0
                forgets_set.remove(w)
                know_set.add(w)
                total += know[w]
        else :
            bit = 1<<dic[x]
            chars &= ~bit
            for w in know_set :
                if w & bit :
                    temp.append(w)
            for w in temp :
                forgets[w] = know[w]
                know[w] = 0
                know_set.remove(w)
                forgets_set.add(w)
                total -= forgets[w]
        answer.append(total)
    return answer

if __name__ == "__main__" :
    print(*solution(), sep='\n')