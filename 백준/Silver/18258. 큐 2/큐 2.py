from collections import deque
from sys import stdin

n = int(input())
que = deque()
for _ in range(n):
    mode, *num = stdin.readline().split()
    if mode == 'push':
        que.append(num[0])
    elif mode == 'pop':
        if len(que) == 0: print(-1)
        else:
            print(que.popleft())
    elif mode == 'size':
        print(len(que))
    elif mode == 'empty':
        print(1) if len(que) == 0 else print(0)
    elif mode == 'front':
        if len(que) == 0: print(-1)
        else:
            print(que[0])
    elif mode == 'back':
        if len(que) == 0: print(-1)
        else:
            print(que[-1])