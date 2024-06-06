def solution(array, commands):
    answer = []
    for i in commands: 
        com = array[i[0]-1:i[1]]
        com.sort()
        answer.append(com[i[2]-1])
    return answer