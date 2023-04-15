def solution(S):
    answer = [0, 0, 0, 0]
    time = {63: 0, 6: 1, 91: 2, 79: 3, 102: 4, 109: 5, 124: 6, 7: 7, 127: 8, 111: 9}
    temp = 0
    # A B C D E F G
    # 0 1 2 3 4 5 6
    for i in range(7):
        if i in [4]:
            continue
        temp |= 1 << i
    print(temp)

    for i, s in enumerate(S):
        temp = 0
        for j, t in enumerate(s):
            if not t:
                continue
            temp |= 1 << j
        answer[i] = time[temp]
    return answer


if __name__ == "__main__":
    S = [
        [1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 0],
        [1, 0, 1, 1, 0, 1, 1],
        [1, 0, 1, 1, 0, 1, 1],
    ]
    print(solution(S))
