from collections import deque
from sys import stdin

left = deque(input())
right = deque()

n = int(input())
for _ in range(n):
    mode, *ch = stdin.readline().split()

    if mode == 'L' and left:
        right.appendleft(left.pop())
    elif mode == 'D' and right:
        left.append(right.popleft())
    elif mode == 'B' and left:
        left.pop()
    elif mode == 'P':
        left.append(ch[0])

print(''.join(left+right))