from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    answer = []
    count, day = 0, 1
    
    while progresses:
        if progresses[0] + speeds[0] * day >= 100:
            count += 1
            progresses.popleft()
            speeds.popleft()
            continue
        elif count > 0:
            answer.append(count)
            count = 0
        day += 1
        
    answer.append(count)
    return answer
            
# 복습 겸 deque 사용해 시간복잡도 O(n)으로 줄임