# 14370 전화번호 수수께끼 (Large) G4

from collections import Counter


def solution() :
    T = int(input())
    answer = []
    
    alphas = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    only = [(0, "Z"), (2, "W"), (4, "U"), (6, "X"), (3, "R"), (7, "S"), (5, "F"), (8, "G"), (1, "O"), (9, "N")]
    nums = []
    for alpha in alphas :
        nums.append(Counter(alpha))


    for t in range(1, T+1) :
        count = Counter()
        word = input()
        for w in word :
            count[w] += 1
        ans = []
        for n, o in only :
            if o not in count :
                continue
            while count[o] :
                count -= nums[n]
                ans.append(str(n))
        ans.sort()
        answer.append(f'Case #{t}: {"".join(ans)}')
    return answer

if __name__ == "__main__" :
    print(*solution(), sep="\n")