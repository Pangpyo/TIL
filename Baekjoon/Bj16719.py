# 16719 ZOAC G5

def solution() :
    word = input()
    n = len(word)
    ans = []
    pre = ['']*n
    for i in range(n) :
        temp = 'Z'*(i+1)
        use = 0
        for j in range(n) :
            if pre[j] :
                continue
            pre[j] = word[j]
            next = ''.join(pre)
            if temp > next :
                use = j
                temp = next
            pre[j] = ''
        pre[use] = word[use]
        ans.append(temp)
            
    return ans

if __name__ == "__main__" :
    print(*solution(), sep="\n")