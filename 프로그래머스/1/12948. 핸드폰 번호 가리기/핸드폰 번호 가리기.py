def solution(phone_number):
    arr = str(phone_number)
    return '*' * (len(arr) - 4) + arr[-4:]