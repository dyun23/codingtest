import sys
sys.setrecursionlimit(10**6)

link = {}

n = int(input())
for _ in range(n - 1):
    a, b = map(int, input().split())
    if a not in link: link[a] = [b]
    else: link[a].append(b)
    if b not in link: link[b] = [a]
    else: link[b].append(a)

parents = [0] * (n - 1)
visited = set()

def find(node):
    visited.add(node)

    for next_node in link[node]:
        if next_node not in visited:
            parents[next_node - 2] = node
            find(next_node)

find(1)
for parent in parents: print(parent)