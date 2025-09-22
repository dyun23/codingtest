def solution(x):
    arr = [int(ch) for ch in str(x)]
    return x % sum(arr) == 0