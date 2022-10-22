# 9934 완전 이진 트리 S1


K = int(input())

nodes = list(map(int, input().split()))

tree = [[] for _ in range(K)]

# 이 문제에 주어진 노드의 순서는 노드를 중위순회 한 순서이다.
def middle(node, k):  # 이 값들중 가장 가운데 값이 루트노드가 된다.
    l = len(node)
    if l == 1:
        tree[-1].append(node[0])
        return
    left = node[0 : l // 2]  # 루트노드와 루트 노드 기준 왼쪽, 오른쪽으로 나눈다.
    mid = node[l // 2]
    right = node[l // 2 + 1 : :]
    tree[-k].append(mid)  # 깊이에 해당하는 노드들을 어펜드 해준다.
    middle(left, k - 1)  # 루트 노드 기준 왼쪽, 오른쪽으로 나눈 노드들의 가운데 노드를 다시 구해준다.
    middle(right, k - 1)


middle(nodes, K)

for t in tree:  # 깊이별로 출력
    print(*t)
