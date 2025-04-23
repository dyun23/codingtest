n = int(input())

next_num = 1
stack = []
answer = []
is_valid = True

for _ in range(n):
    num = int(input())

    while next_num <= num:
        stack.append(next_num)
        answer.append('+')
        next_num += 1

    if stack and stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        is_valid = False
        break

if is_valid:
    for i in answer:
        print(i)
else:
    print('NO')