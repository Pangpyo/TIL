def solution(sizes, limits, tasks) :
    answer = []
    for size, limit, task in zip(sizes, limits, tasks) :
        time = int(task[0]) * (size ** (len(task)-1))
        answer.append(int(limit >= time))
    return answer


print(solution([10, 2, 13, 1], [300, 31, 100, 5], ["3tt", "4ttt", "8t", "4tttt"]))