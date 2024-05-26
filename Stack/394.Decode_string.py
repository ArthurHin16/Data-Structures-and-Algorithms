# Given an encoded string, return its decoded string.

def decodeString(s):
    stack = []
    current_num = 0
    current_str = ''

    for c in s:
        if c.isdigit():
            current_num = current_num * 10 + int(c) #Transform string into a number
        elif c == '[':
            stack.append((current_str, current_num))
            current_str = ''
            current_num = 0
        elif c == ']':
            last_str, num = stack.pop()
            current_str = last_str + num * current_str
        else:
            current_str += c
    return current_str


s = "2[abc]3[cd]ef"
print(decodeString(s))
