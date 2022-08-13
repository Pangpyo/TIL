# 1208 Flatten D3

import sys

sys.stdin = open("_Flatten.txt")

for i in range(1, 11) :
    dump = int(input())
    boxs = list(map(int, input().split()))
    for _ in range(dump) :
        boxs[boxs.index(max(boxs))] -= 1 # 가장 높은 박스를 하나 빼주고
        boxs[boxs.index(min(boxs))] += 1 # 가장 낮은 박스는 하나 더해준다.
    print('#%d'%i, max(boxs)-min(boxs)) # 가장 높은 박스와 낮은 박스의 차이를 출력한다
