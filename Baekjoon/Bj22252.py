# 22252 정보 상인 호석 G5

from collections import defaultdict
from heapq import heappop, heappush
import sys


def solution() :
    input = sys.stdin.readline
    N = int(input())
    goril = defaultdict(list)
    def get(query) :
        name = query[1]
        for c in map(int, query[3::]) :
            heappush(goril[name], -c)
        return 0
    def buy(query) :
        name = query[1]
        b = int(query[2])
        info = goril[name]
        money = 0
        cnt = 0
        while info and cnt < b :
            money += -heappop(info)
            cnt += 1
        return money
    answer = 0
    func = {"1" : get, "2" : buy}
    for _ in range(N) :
        query = tuple(input().split())
        answer += func[query[0]](query)
    return answer

if __name__ == "__main__" :
    print(solution())