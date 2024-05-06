"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t
(i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
"""

def gcdOfStrings(str1, str2):
    len1, len2 = len(str1), len(str2)
        
    def isDivisor(l):
        if len1 % l or len2 % l:
            return False
        factor1, factor2 = len1 // l, len2 // l
        return str1[:l] * factor1 == str1 and str1[:l] * factor2 == str2

    for l in range(min(len1, len2), 0, -1):
        if isDivisor(l):
            return str1[:l]

    return ""

str1 = "ABCABC"
str2 = "ABC"
print(gcdOfStrings(str1, str2))