# 2922 즐거운 단어 G4

def solution():
    word = input()
    N = len(word)
    answer = 0
    temp = [""]*N
    VOWELS = "AEIOU"
    V = 'V'
    C = 'C'
    L = 'L'
    def dfs(n, cnt):
        nonlocal answer
        if n >= 3:
            vs = 0
            for i in range(n-3, n):
                if temp[i] == V:
                    vs += 1
            if vs == 0 or vs == 3:
                return
        if n == N:
            if L in temp:
                answer += cnt
            return
        if word[n] == '_':
            temp[n] = V
            dfs(n+1, cnt*5)
            temp[n] = C
            dfs(n+1, cnt*20)
            temp[n] = L
            dfs(n+1, cnt)
        else:
            if word[n] == L:
                temp[n] = L
            elif word[n] in VOWELS:
                temp[n] = V
            else:
                temp[n] = C
            dfs(n+1, cnt)
    dfs(0, 1)
    return answer

if __name__ == "__main__":
    print(solution())