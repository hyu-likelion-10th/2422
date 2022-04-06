from bwsi_grader.python.palindrome import grader

# make sure to execute this cell so that your function is defined
# you must re-run this cell any time you make a change to this function

def student_func(x):
    # `x` is a string
    # this function should return either `True` or `False`
    
    # write your code here
    # be sure to include a `return` statement so that
    # your function returns the appropriate object.
    x = x.replace(' ', '')
    for count, i in enumerate(x[0:int(len(x) / 2) + 1]):
        j = x[len(x) - 1 - count]
        if i == j or ord(i) == ord(j) + 32 or ord(j) == ord(i) + 32:
            flag = True
        else:
            flag = False
            return flag
    return flag

grader(student_func)