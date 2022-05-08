def backward(number):
    new_number = 0
    while number > 0:
        new_number = 10 * new_number + number%10
        number = number // 10
    return new_number


def solution(first, second):
    if backward(first) > backward(second):
        return backward(first)
    else:
        return backward(second)

first, second = input().split()
first = int(first)
second = int(second)

print(solution(first, second))