def solution(arr):
    answer = [arr[0]]
    arr.pop(0)
    while 1:
        for i in arr:
            if i != answer[-1]: answer.append(i)
            
        break;
        
    return answer