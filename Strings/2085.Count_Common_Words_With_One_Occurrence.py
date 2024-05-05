#Given two string arrays words1 and words2, return the number of strings that appear exactly 
#once in each of the two arrays.

from collections import defaultdict

def countWords(words1, words2):
        hashmap_1 = defaultdict(int)
        hashmap_2 = defaultdict(int)

        for s in words1:
            hashmap_1[s] += 1
        for s in words2:
            hashmap_2[s] += 1

        set_1 = set()
        set_2 = set()
        for key, value in hashmap_1.items():
            if value == 1:
                set_1.add(key)
        
        for key, value in hashmap_2.items():
            if value == 1:
                set_2.add(key)

        return len(set_1 & set_2) # & -> Intersection: find the common elements between two sets

words1 = ["leetcode","is","amazing","as","is"]
words2 = ["amazing","leetcode","is"]
print(countWords(words1, words2))