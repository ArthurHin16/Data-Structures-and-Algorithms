"""
You are given a string s, which contains stars *.
In one operation, you can:
- Choose a star in s.
- Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.
Note:
- The input will be generated such that the operation is always possible.
- It can be shown that the resulting string will always be unique.
"""
import timeit

def removeStars(s):
    stack = []
    for c in s:
        if c == "*":
            stack.pop()
        else:
            stack.append(c)
    return "".join(stack)

s = "leet**cod*e"

execution_time = timeit.timeit(lambda: removeStars(s), number=10000)
print("Execution time: {:.2f} milliseconds".format(execution_time * 1000))