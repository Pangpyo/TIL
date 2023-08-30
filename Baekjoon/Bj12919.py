# 12919 A와 B 2 G5

def solution() :
    S = input()
    T = input()
    answer = 0
    def dfs(word, rev) :
        nonlocal answer
        if answer :
            return
        if len(word) == len(S) :
            if (not rev and word == S) or (rev and word[::-1] == S):
                answer = 1
            return
        if rev :
            if word[0] == 'A' :
                dfs(word[1::], rev)
            if word[-1] == 'B' :
                dfs(word[0:-1], not rev)
        else :
            if word[-1] == 'A' :
                dfs(word[0:-1], rev)
            if word[0] == 'B' :
                dfs(word[1::], not rev)
    dfs(T, False)
    return answer

if __name__ == "__main__" :
    print(solution())