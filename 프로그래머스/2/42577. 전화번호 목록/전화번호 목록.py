def solution(book):
    book.sort()
    for i in range(len(book)-1):
        if book[i] == book[i + 1][:len(book[i])]: return False
    return True