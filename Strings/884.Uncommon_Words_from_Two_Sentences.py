"""
A sentence is a string of single-space separated words where each 
word consists only of lowercase letters.
A word is uncommon if it appears exactly once in one of the sentences,
and does not appear in the other sentence.
Given two sentences s1 and s2, return a list of all the uncommon words. 
You may return the answer in any order.
"""

def uncommonFromSentences(s1, s2):
        s1 = s1.split()
        s2 = s2.split()
        words = {}
        result = []

        for s in s1:
            if s not in words:
                words[s] = 1
            else:
                words[s] += 1
        
        for s in s2:
            if s not in words:
                words[s] = 1
            else:
                words[s] += 1
        
        for key, value in words.items():
            if value == 1:
                result.append(key)
        return result

s1 = "this apple is sweet"
s2 = "this apple is sour"
print(uncommonFromSentences(s1, s2))