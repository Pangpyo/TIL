# Dev Matching 백엔드 행렬 테두리 회전하기


def solution(rows, columns, queries):
    matrix = [[0] * columns for _ in range(rows)]
    answer = []
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = i * columns + j + 1
    for query in queries:
        for i in range(4):
            query[i] -= 1
        x1, y1, x2, y2 = query
        a = matrix[x1][y1]
        nums = []
        for i in range(1, y2 - y1 + 1):
            b = matrix[x1][y1 + i]
            matrix[x1][y1 + i] = a
            nums.append(a)
            a = b
        for i in range(1, x2 - x1 + 1):
            b = matrix[x1 + i][y2]
            matrix[x1 + i][y2] = a
            nums.append(a)
            a = b
        for i in range(1, y2 - y1 + 1):
            b = matrix[x2][y2 - i]
            matrix[x2][y2 - i] = a
            nums.append(a)
            a = b
        for i in range(1, x2 - x1 + 1):
            b = matrix[x2 - i][y1]
            matrix[x2 - i][y1] = a
            nums.append(a)
            a = b
        answer.append(min(nums))

    return answer


rows = 6
columns = 6
queries = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]


print(solution(rows, columns, queries))
