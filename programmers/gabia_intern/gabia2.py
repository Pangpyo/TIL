from heapq import heappop, heappush

def solution(req_id, req_info):
    peaple = {}
    print(peaple)
    answer = []
    sell_heap = []
    buy_heap = [] # 0 : 가격(-), 1 : 순서, 2 : 양, 3 : 이름
    idx = 1
    for info, id in zip(req_info, req_id) :
        if id not in peaple :
            peaple[id] = [0, 0]
        print(info, id)
        if info[0] == 1 :
            can_sell = True
            sell_amount = info[1]
            sell_price = info[2]
            while can_sell :
                can_sell = False
                if buy_heap and buy_heap[0][0] >= -sell_price :
                    amount = min(buy_heap[0][2], sell_amount)
                    if buy_heap[0][2] > sell_amount :
                        buy_heap[0][2] -= sell_amount
                        sell_amount = 0
                    elif buy_heap[0][2] < sell_amount :
                        sell_amount -= buy_heap[0][2]
                        can_sell = True
                    peaple[buy_heap[0][3]][0] += amount
                    peaple[buy_heap[0][3]][1] -= amount*sell_price
                    peaple[id][0] -= amount
                    peaple[id][1] += amount*sell_price
                    if not buy_heap[0][2] :
                        heappop(buy_heap)
            if sell_amount :
                heappush(sell_heap, [sell_price, idx, sell_amount, id])
        else :
            can_buy = True
            buy_amount = info[1]
            buy_price = info[2]
            while can_buy :
                can_buy = False
                if sell_heap and sell_heap[0][0] <= buy_price :
                    amount = min(sell_heap[0][2], buy_amount)
                    if sell_heap[0][2] > buy_amount :
                        sell_heap[0][2] -= buy_amount
                        buy_amount = 0
                    elif sell_heap[0][2] < buy_amount :
                        buy_amount -= sell_heap[0][2]
                        can_buy = True
                    peaple[sell_heap[0][3]][0] += amount
                    peaple[sell_heap[0][3]][1] -= amount*buy_price
                    peaple[id][0] -= amount
                    peaple[id][1] += amount*buy_price
                    if not sell_heap[0][2] :
                        heappop(sell_heap)
            if buy_amount :
                heappush(buy_heap, [buy_price, idx, buy_amount, id])
        idx += 1
    print(sell_heap)
    return answer

req_id = ["William", "Andy", "Rohan", "Rohan", "Louis", "Andy"]
req_info = [[1, 7, 20], [0, 10, 10], [1, 10, 40], [1, 4, 25], [0, 5, 11], [0, 20, 30]]

print(solution(req_id, req_info))