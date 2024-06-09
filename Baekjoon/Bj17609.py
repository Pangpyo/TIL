# 17609 회문 G5

def solution():
    T = int(input())
    answer = [2]*T
    for t in range(T):
        word = input()
        if word == word[::-1]:
            answer[t] = 0
        else:
            s, e = 0, len(word)-1
            while s <= e:
                if word[s] == word[e]:
                    s += 1
                    e -= 1
                else:
                    if word[s+1] == word[e]:
                        temp = word[:s] + word[s+1:]
                        if temp == temp[::-1]:
                            answer[t] = 1
                    if word[s] == word[e-1]:
                        temp = word[:e] + word[e+1:]
                        if temp == temp[::-1]:
                            answer[t] = 1
                    break
    return answer

if __name__ == "__main__":
    print(*solution(), sep='\n')