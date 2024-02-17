from collections import defaultdict


def solution(nodes, edges) :
    answer = [0, 0]
    graph = defaultdict(list)
    for u, v in edges :
        graph[u].append(v)
        graph[v].append(u)
    forests = []
    visit = set()
    def dfs(n) :
        forest.append(n)
        visit.add(n)
        for nn in graph[n] :
            if nn not in visit :
                dfs(nn)
    for node in nodes :
        if node not in visit :
            forest = []
            dfs(node)
            forests.append(forest)
    def is_tree(forest, is_forward) :
        root = 0
        for node in forest :
            if (node%2 == (len(graph[node])-1)%2) != is_forward :
                root += 1
        if root == 1 :
            return True
        else :
            return False
    for forest in forests :
        answer[0] += is_tree(forest, True)
        answer[1] += is_tree(forest, False)
    return answer

print(solution([9, 15, 14, 7, 6, 1, 2, 4, 5, 11, 8, 10], [[5, 14], [1, 4], [9, 11], [2, 15], [2, 5], [9, 7], [8, 1], [6, 4]]))