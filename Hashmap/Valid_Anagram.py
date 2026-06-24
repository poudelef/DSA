# Valid Anagram

# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"
# Output: true

# Example 2:

# Input: s = "jar", t = "jam"
# Output: false

def valid_anagram(s:str, t:str) -> bool:
    if len(s) != len(t):
        return False
    h= {}
    for i in range(len(s)): # O(n) time
        h[s[i]] = h.get(s[i], 0) + 1

    for j in range(len(t)): # O(n) time
        h[t[j]]  = h.get(t[j], 0) - 1

    for v in h.values(): # O(n) time
        if v!=0:
            return False
    return True           

# Time Complexicity = O(n) + O(n) + O(n) = 3O(n) = O(n)
# Space Complexicity = O(n) as we have created one hashmap           


print(valid_anagram("jar", "jam"))    

# WE can further improve this and make it clean by using only one loop. 
# This also has Time and Space as O(1) but it looks cleaner with one loop only

def valid_anagram_2nd(s:str, t:str)->bool:
    if len(s) != len(t):
        return False
    s_h = {}
    t_h = {}
    for i in range(len(s)):
        s_h[s[i]] = s_h.get(s[i], 0) + 1    
        t_h[t[i]] = t_h.get(t[i], 0 ) + 1

    return s_h == t_h

print(valid_anagram_2nd("jffr", "jrff"))            