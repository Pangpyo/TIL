# 2831 댄스 파티 G4

def solution():
    N = int(input())
    set1 = [[], []]
    set2 = [[], []]
    for m in map(int, input().split()):
        if m < 0:
            set1[1].append(-m)
        else:
            set2[0].append(m)
    for w in map(int, input().split()):
        if w < 0:
            set2[1].append(-w)
        else:
            set1[0].append(w)
    set1[0].sort()
    set1[1].sort()
    set2[0].sort()
    set2[1].sort()
    answer = 0
    def match(arr):
        idx = 0
        answer = 0
        for m in arr[0]:
            while idx < len(arr[1]):
                if arr[1][idx] > m:
                    answer += 1
                    idx += 1
                    break
                idx += 1
        return answer
    answer = match(set1) + match(set2)
    return answer

if __name__ == "__main__":
    print(solution())