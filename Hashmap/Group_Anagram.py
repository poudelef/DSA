# Group Anagrams

# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
from collections import defaultdict

def group_anagram(strs:list)->list:
    h= defaultdict(list)
    for i in range(len(strs)):
        s_words = tuple(sorted(strs[i]))
        h[s_words].append(strs[i])   
    return list(h.values())


print(group_anagram(["act","pots","tops","cat","stop","hat"]))        


# notes:
# Dictonary key must be hashable (immutable)

# These can be dictionary keys:
# "hello"      # string
# 123          # int
# (1, 2, 3)    # tuple

# These cannot:
# [1, 2, 3]    # list
# {"a": 1}     # dict
# {1, 2, 3}    # set