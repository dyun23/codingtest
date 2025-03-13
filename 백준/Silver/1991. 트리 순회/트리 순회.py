tree = {}

n = int(input())
for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]

pre, inorder, post = '', '', ''

def order(node):
    global pre, inorder, post
    if node == '.':
        return
    pre += node
    order(tree[node][0])
    inorder += node
    order(tree[node][1])
    post += node

order('A')

print(pre)
print(inorder)
print(post)