# Valid Palindrome

# Given a string s, return true if it is a palindrome, otherwise return false.
# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
# Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

# Example 1:
# Input: s = "Was it a car or a cat I saw?"
# Output: true

def valid_palindrome(s:str)->bool:
    alphaN= []
    for word in s: # O(n)
        if word.isalnum():
            alphaN.append(word) 

    cleaned_word = ("".join(alphaN)).lower() # join runs O(n) and lower runs O(n)
    l = 0 
    r = len(cleaned_word) - 1
    while l <= r: # O(n) / 2
        if cleaned_word[l] != cleaned_word[r]:
            return False
        l += 1
        r -= 1
    return True        

# Time Complexicity is O(n) + O(n) + O(n) + O(n)/2 = O(n)
# Space Complexixity is O(n)
   


s = "asdfghhgfdsasdsdsdvv"
print(valid_palindrome(s))
