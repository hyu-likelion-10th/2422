# Problem 2. 평균은 넘겠지(4344)

def solution():
    C = int(input()) # 테스트 케이스의 개수
    for _ in range(C):
        case = list(map(int, input().split()))
        avr = sum(case[1::]) / case[0]
        percent = sum(1 for score in case[1::] if score > avr) / case[0] * 100.0
        print("%.3f" %percent, end = '')
        print("%")

if __name__ == '__main__':
    solution()
