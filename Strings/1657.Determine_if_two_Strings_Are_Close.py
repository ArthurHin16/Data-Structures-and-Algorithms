"""
Two strings are considered close if you can attain one from the other using the following operations:
Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.
Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
"""
from collections import Counter

def closeStrings(word1, word2):
    if len(word1) != len(word2):
        return False

    if word1 == word2:
        return True

    c1 = Counter(word1)
    c2 = Counter(word2)
    result = all([sorted(c1.values()) == sorted(
        c2.values()), set(c1) == set(c2)])

    return result

word1 = "abc"
word2 = "bca"
print(closeStrings(word1, word2))
