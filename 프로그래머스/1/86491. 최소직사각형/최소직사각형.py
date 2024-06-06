def solution(sizes):
    a, b = [], []
    for i in sizes:
        i.sort(reverse = True)
        a.append(i[0])
        b.append(i[1])
    return max(a) * max(b)