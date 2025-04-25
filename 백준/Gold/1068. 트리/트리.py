import sys
sys.setrecursionlimit(10**6)

def dsf(node):
    if len(tree[node]) == 0:
        leef.append(node)
    else:
        for i in tree[node]:
            dsf(i)

n = int(input())
parent = list(map(int, input().split()))
tree = {}
root = 0

for i in range(n):
    if parent[i] == -1:
        root = i
    else:
        if parent[i] not in tree:
            tree[parent[i]] = []
        tree[parent[i]].append(i)
    if i not in tree: tree[i] = []

delete = int(input())

if delete == root:
    print(0)
else:
    tree[parent[delete]].remove(delete)
    tree.pop(delete)

    leef = []
    dsf(root)
    print(len(leef))