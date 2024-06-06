def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = [0, 0, 0]
    result = []
    
    for i, val in enumerate(answers):
        if val == a[i % 5]: answer[0] += 1
        if val == b[i % 8]: answer[1] += 1 
        if val == c[i % 10]: answer[2] += 1 
        
    for i in range(0,3):
        if max(answer) == answer[i]: result.append(i+1)
        
    return result