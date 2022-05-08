# import numpy as np

def start():
    testcase_number = int(input())
    students = []
    for i in range(testcase_number):
        single_case = list(map(int, input().split()))
        single_case.pop(0)
        students.append(single_case)
    
    solution(students)
    

def solution(students):
    for x in students:
        # average = np.mean(x)
        average = sum(x) / len(x)
        counter = 0
        for y in x:
            if y > average:
                counter += 1
        print("{:.3f}%".format(counter / len(x) * 100))

start()