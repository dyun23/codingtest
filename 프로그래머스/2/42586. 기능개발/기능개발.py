def solution(progresses, speeds):
    answer = []
    day, end = 0, 0
    
    while len(progresses)> 0:
        if (progresses[0] + speeds[0]*day) >= 100: 
            progresses.pop(0)
            speeds.pop(0)
            end += 1
        elif end > 0: 
            answer.append(end)
            end = 0
            day += 1
        else:
            day += 1
            
    answer.append(end)
    return answer