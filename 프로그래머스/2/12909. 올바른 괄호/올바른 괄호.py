def solution(s):

    count = 0
    
    for i in s:
        if count < 0: return False
        elif i == '(':
            count += 1
        else:
            count -= 1
    return True if count == 0 else False