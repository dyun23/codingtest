from itertools import combinations
from collections import Counter
def solution(clothes):
    item = dict(Counter(dict(clothes).values()))
    # result = len(clothes)
    # result += sum([eval('*'.join(map(str, c)))  for i in range(2, len(item)+1) for c in combinations(item.values(), i)])
    
    result = 1
    values = list(item.values())
    for i in values:
        result *= i + 1
        
    return result - 1