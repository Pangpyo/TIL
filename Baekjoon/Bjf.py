# F 가희와 클럽 오디션 2


def solution():
    directions = {
        'W': 8, 'A': 4, 'S': 2, 'D': 6,
        'LU': 7, 'LD': 1, 'RU': 9, 'RD': 3
    }
    reverse_directions = {
        'W': 'S', 'A': 'D', 'S': 'W', 'D': 'A',
        'LU': 'RD', 'LD': 'RU', 'RU': 'LD', 'RD': 'LU'
    }
    input_str = input()
    my_input = input()
    parsed_result = []
    i = 0
    while i < len(input_str):
        direction = ''
        if input_str[i] in ['W', 'A', 'S', 'D']:
            direction += input_str[i]
            i += 1
        elif input_str[i:i + 2] in ['LU', 'LD', 'RU', 'RD']:
            direction += input_str[i:i + 2]
            i += 2
        reverse = ''
        if i < len(input_str) and input_str[i] == '!':
            reverse = '!'
            i += 1
        if reverse:
            if len(direction) == 1:
                direction = reverse_directions[direction]
            else:
                direction = reverse_directions[direction]
        parsed_result.append(directions.get(direction))
    idx = 0
    N = len(parsed_result)
    for c in my_input :
        if not c.isdigit() :
            c = directions[c]
        else :
            c = int(c)
        if idx < N and c == parsed_result[idx] :
            idx += 1
        else :
            idx = 0
    if idx == N :
        return "Yes"
    else :
        return "No"


if __name__ == "__main__" :
    print(solution())