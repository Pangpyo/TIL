# 9934 완전 이진 트리 S1


K = int(input())

nodes = list(map(int, input().split()))

tree = [[] for _ in range(K)]


def middle(node, k):
    l = len(node)
    if l == 1:
        tree[-1].append(node[0])
        return
    left = node[0 : l // 2]
    mid = node[l // 2]
    right = node[l // 2 + 1 : :]
    tree[-k].append(mid)
    middle(left, k - 1)
    middle(right, k - 1)


middle(nodes, K)

for t in tree:
    print(*t)
