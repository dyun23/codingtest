from collections import deque

n = int(input())
answer = list()

for _ in range(n):
    pw = list(input())
    left = deque()
    right = deque()
    
    for ch in pw:
        if ch == '<':
            if left: right.appendleft(left.pop())
        elif ch == '>':
            if right: left.append(right.popleft())
        elif ch == '-':
            if left: left.pop()
        else:
            left.append(ch)
    answer.append(''.join(left + right))

for i in answer:
    print(i)