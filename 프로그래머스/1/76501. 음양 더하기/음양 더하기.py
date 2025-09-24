def solution(absolutes, signs):
    return sum(i if sign else -i for i, sign in zip(absolutes, signs))