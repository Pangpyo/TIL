# Summer/Winter Coding(~2018) 스티커 모으기(2)


def solution(sticker):
    answer = []
    N = len(sticker)
    D = [0] * N
    D[0] = sticker[0]
    for i in range(1, N - 1):
        D[i] = sticker[i] + max(D[i - 2], D[i - 3])
    answer.append(max(D))
    if N >= 2:
        D = [0] * N
        D[1] = sticker[1]
        for i in range(2, N):
            D[i] = sticker[i] + max(D[i - 2], D[i - 3])
        answer.append(max(D))

    return max(answer)
