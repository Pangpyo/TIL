# 1874 스택 수열 S2
import sys
input = sys.stdin.readline

N = int(input())
seq = []
for i in range(N) :
    seq.append(int(input()))
stack = []
nums = []
answer = []
j = 0
for i in range(1, N+1) :
    nums.append(i)
    answer.append('+')
    while nums :
        if nums[-1] == seq[j] :
            stack.append(nums.pop())
            answer.append('-')
            j += 1
        else :
            break

if stack == seq :
    print(*answer, sep='\n')
else :
    print('NO')
