def solution(line):
    n = len(line)
    ans = [line[0]]
    pre = line[0]
    for i in range(1, n):
        if line[i] != pre:
            ans.append(line[i])
            pre = line[i]
        else:
            if ans[-1] != "*":
                ans.append("*")
    answer = "".join(ans)
    return answer
