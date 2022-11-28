# 데브매칭 1번


def solution(low, high, img):
    N = len(img)
    M = len(img[0])
    answer = 0

    def isqr(start, end, x, low, high):
        M = len(img[0])
        N = len(img)
        if x + end - start >= N:
            return 0
        if img[x + end - start][start : end + 1].count("."):
            return 0
        black = 0
        for i in range(x, x + end - start + 1):
            print("def", i, img[i][start], img[i][end])
            if img[i][start] == "#" and img[i][end] == "#":
                print("can", i, start, end)
                black += img[i][start : end + 1].count("#")
            else:
                return 0
        print(black)
        black -= (end - start + 1) ** 2 - (end - start - 1) ** 2
        print(black)
        print((black) / ((end - start + 1) ** 2) * 100)
        if low <= (black) / ((end - start - 1) ** 2) * 100 < high:
            return 1

    for i in range(N):
        start = -1
        end = -1
        can = False
        cnt = 0
        for j in range(M):
            if not can:
                if img[i][j] == "#":
                    can = True
                    cnt = 1
                    start = j
            else:
                if img[i][j] == "#":
                    cnt += 1
                    end = j
                else:
                    start = -1
                    end = -1
                    can = False
                    cnt = 0
            if cnt >= 3:
                print(i, start, end, img[i][start : end + 1])
                if isqr(start, end, i, low, high):
                    print("answer", start, end, i)
                    answer += 1

    return answer


low = 25
high = 51
img = [
    ".########......",
    ".####...#......",
    ".#.####.#.#####",
    ".#.#..#.#.#..##",
    ".#.##.#.#.#...#",
    ".#.####.#.#...#",
    ".#....###.#####",
    ".########......",
]

print(solution(low, high, img))
