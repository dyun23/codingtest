def solution(s):
    stack = []
    for i in list(s):
        if i == '(':
            stack.append(0)
        elif stack:
            stack.pop()
        else:
            return False
        
    return False if stack else True