# Problem 1. 상수(2908)

def solution():
    # A, B: 세 자리 정수
    A, B = map(int, input().split())
    return max(int(str(A)[::-1]), int(str(B)[::-1]))

if __name__ == '__main__':
    print(solution())
