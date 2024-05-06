"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.
"""
def mergeAlternately(word1, word2):

    new_string = ""
    len_word1 = len(word1) - 1
    len_word2 = len(word2) - 1

    p1 = 0
    p2 = 0

    while p1 <= len_word1 and p2 <= len_word2:
        new_string += word1[p1]
        new_string += word2[p2]
        p1 += 1
        p2 += 1

    if p1 <= len_word1:
        new_string += word1[p1:]
    else:
        new_string += word2[p2:]

    return new_string 

word1 = "gmumn"
word2 = "azia"
print(mergeAlternately(word1, word2))