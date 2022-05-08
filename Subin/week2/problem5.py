
def solution(phone_book):
    counter = 0
    answer = True
    for i in phone_book:
        for j in phone_book[counter + 1:]:
            if j.startswith(i):
                answer = False
                return answer
        counter += 1
    
    return answer