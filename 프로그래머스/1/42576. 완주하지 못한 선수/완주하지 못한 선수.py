# 해시 사용
def solution(participant, completion):
    dict = {}
    for i in participant:
        if i in dict: dict[i] += 1
        else: dict[i] = 1
    for i in completion: dict[i] -= 1
    for i in dict:
        if dict[i] > 0: return i
        
# 정렬 사용
# def solution(participant, completion):
#     participant.sort();
#     completion.sort();
#     for a, b in zip(participant, completion):
#         if a != b: return a
#     return participant[-1]