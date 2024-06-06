def solution(priorities, location):
    answer = 0
    pri_index = [[priorities[i], i] for i in range(len(priorities))]
    
    while pri_index:
        if pri_index[0][0] == max(pri_index, key=lambda x:x[0])[0]:
            answer += 1
            if pri_index[0][1] == location:
                return answer
            else:
                pri_index.pop(0)
        else:
            pri_index.append(pri_index.pop(0))