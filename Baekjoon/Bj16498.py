# 16498 작은 벌점 G5

def solution():
    A, B, C = map(int, input().split())
    cards = [sorted(list(map(int, input().split()))) for _ in range(3)]
    INF = float('inf')
    answer = INF
    def binary_search(n, arr):
        s, e = 0, len(arr)-1
        diff = INF
        res = 0
        while s <= e:
            m = (s+e)//2
            d = arr[m] - n
            if abs(d) < diff:
                diff = abs(d)
                res = arr[m]
            if d > 0:
                e = m - 1
            elif d < 0:
                s = m + 1
            else:
                return arr[m]
        return res
    def score(a, b, c):
        return abs(max(a, b, c)-min(a, b, c))
    for a in cards[0]:
        b = binary_search(a, cards[1])
        ac = binary_search(a, cards[2])
        bc = binary_search(b, cards[2])
        answer = min(answer, score(a, b, ac), score(a, b, bc))
    return answer

if __name__ == "__main__":
    print(solution())