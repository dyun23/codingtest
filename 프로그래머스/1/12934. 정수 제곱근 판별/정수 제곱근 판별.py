def solution(n):
    i = n ** 0.5
    if i % 1 == 0:
        return (i + 1) **2
    else: return -1