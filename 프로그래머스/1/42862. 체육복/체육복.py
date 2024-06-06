def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    
    _reserve.sort()
    _lost.sort()
    
    for i in _lost:
        if i-1 in _reserve:
            _reserve.remove(i-1)
        elif i+1 in _reserve: 
            _reserve.remove(i+1)
        else: n -= 1
    return n