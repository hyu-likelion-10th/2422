# Problem 4. 완주하지 못한 선수(42576)

def solution(participant, completion):
    p, c = sorted(participant), sorted(completion)
    for pair in zip(p, c):
        if pair[0] != pair[1]:
            return pair[0]
    return p[-1]
