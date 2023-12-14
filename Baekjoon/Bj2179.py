# 2179 비슷한 단어 G4

from collections import defaultdict
import sys


def solution() :
    input = sys.stdin.readline
    N = int(input())
    words = [(input().rstrip(), i) for i in range(N)]
    words.sort()
    dic = defaultdict(list)
    for i in range(1, N) :
        pre_word = words[i-1][0]
        word = words[i][0]
        m = len(pre_word)
        same = m
        for j in range(m) :
            if pre_word[j] != word[j] :
                same = j
                break
        same_word = word[0:same]
        if same :
            if not dic[same_word]:
                dic[same_word].append(words[i-1])
            dic[same_word].append(words[i])
            
    answers = []
    for k, v in dic.items() :
        min_idx = float('inf')
        dic[k].sort(key=lambda x : x[1])
        for word, idx in v :
            min_idx = min(min_idx, idx)
        answers.append((k, min_idx))
    answers.sort(key = lambda x : (-len(x[0]), x[1]))
    answer = []
    answer.append(dic[answers[0][0]][0][0])
    answer.append(dic[answers[0][0]][1][0])
    return answer

if __name__ == "__main__" :
    print(*solution(), sep='\n')