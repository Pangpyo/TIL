# 정렬 가장 큰 수


def solution(numbers):
    def big(n):
        ans = str(n) * 4
        return int(ans[:4])

    numbers.sort(key=lambda x: -big(x))
    if numbers[0] == 0:
        return 0
    answer = ""
    for n in numbers:
        answer = "".join([answer, str(n)])
    return answer


numbers = [0, 0, 0]

print(solution(numbers))
