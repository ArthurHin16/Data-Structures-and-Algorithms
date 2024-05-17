"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
"""


def maxVowels(self, s: str, k: int) -> int:
    
    vowels = "aeiou"
    number_vowels = 0

    for i in range(k):
        if s[i] in vowels:
            number_vowels += 1

    max_vowels = number_vowels
    for i in range(k, len(s)):
        if s[i - k] in vowels:
            number_vowels -= 1
        if s[i] in vowels:
            number_vowels += 1
        max_vowels = max(number_vowels, max_vowels)

    return max_vowels
