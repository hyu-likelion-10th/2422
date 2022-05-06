# Problem 5. 전화번호 목록(42577)

def solution(phone_book):
    p = sorted(phone_book)
    for i in range(len(p) - 1):
        if p[i] in p[i+1][0:len(p[i])]:
            return False
    return True
