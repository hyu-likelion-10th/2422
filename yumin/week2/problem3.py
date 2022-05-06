# Problem 3. 단어 공부(1157)

def solution():
    word = input().upper()
    counts = {key: list(word).count(key) for key in set(word)}
    max_values = [key for key in list(counts.keys()) if counts[key] == max(counts.values())]
    if len(max_values) == 1:
        return max_values[0]
    else:
        return '?'

if __name__ == '__main__':
    print(solution())
