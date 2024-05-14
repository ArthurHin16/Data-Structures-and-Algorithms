"""
Given an array of characters chars, compress it using the following algorithm:
Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead,
be stored in the input character array chars. Note that group lengths that are 10 or 
longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.
You must write an algorithm that uses only constant extra space.
"""


def compress(chars):
    write_index = 0
    total = 1
    for i in range(len(chars)):
        if i + 1 < len(chars) and chars[i] == chars[i + 1]:
            total += 1
        else:
            chars[write_index] = chars[i]
            write_index += 1
            if total > 1:
                for char in str(total):
                    chars[write_index] = char
                    write_index += 1
            total = 1
    del chars[write_index:]
    print(chars)
    return write_index


chars = ["a","a", "a", "b","b","b","b","b","b","b","b","b","b","b","b"]
print(compress(chars))
