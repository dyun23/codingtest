def solution(n):
    answer = []
    for i in range(0,n):
        li = []
        for j in range(0,n):
            if i==j: li.append(1)
            else : li.append(0)
        answer.append(li)
    return answer