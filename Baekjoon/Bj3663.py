# 3663 고득점 G3

import sys

def solution():
    input = sys.stdin.readline
    T = int(input())
    answers = [0]*T
    for t in range(T) :
        name = input().rstrip()
        answer = 0
        length = len(name)

        for letter in name:
            answer += min(ord(letter) - ord('A'), abs(ord(letter) - ord('Z') - 1))
        min_move = length - 1
        for i in range(length):
            next_i = i + 1
            while next_i < length and name[next_i] == 'A':
                next_i += 1
            min_move = min(min_move, i + (i + length - next_i), 2 * (length - next_i) + i)
        answer += min_move

        answers[t] = answer
    return answers

if __name__ == "__main__" :
    print(*solution(), sep="\n")