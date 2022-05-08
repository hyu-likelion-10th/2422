from collections import Counter

word = input()
word = word.upper()
counts = Counter(word)
max_value = max(counts.values())

flag = 0
for i in counts.keys():
    if counts[i] == max_value:
        flag += 1

if flag == 1:
    print(list(counts.keys())[list(counts.values()).index(max_value)])
else:
    print("?")