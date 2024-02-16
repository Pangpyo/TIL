# 15831 준표의 조약돌 G4

def solution() :
    N, B, W = map(int, input().split())
    have = [0, 0]
    s = 0
    stone = input()
    answer = 0
    for e in range(N) :
        if stone[e] == "B" :
            have[0] += 1
        else :
            have[1] += 1
        while s <= e and have[0] > B :
            if stone[s] == "B" :
                have[0] -= 1
            else :
                have[1] -= 1
            s += 1
        if have[0] <= B and have[1] >= W :
            answer = max(e-s+1, answer)
    return answer

if __name__ == "__main__" :
    print(solution())