from collections import Counter

def solution(participant, completion):
    p_dict = Counter(participant)
    c_dict = Counter(completion)
    for i in p_dict.keys():
        if p_dict[i] > 1:
            if c_dict[i] != p_dict[i]:
                return i
        
    answer = list(set(participant) - set(completion))
    answer = ''.join(answer)
    return answer