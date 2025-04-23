n = int(input())
answer = list()

for _ in range(n):
    vps = list(input())
    stack = list()
    is_valid = True
    
    for x in vps:
        if x == '(':
            stack.append(0)
        elif x == ')':
            if not stack:
                is_valid = False
                break
            stack.pop()
            
    if stack or is_valid is False: answer.append('NO')
    else: answer.append('YES')

for i in answer:
    print(i)