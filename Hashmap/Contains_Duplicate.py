# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]
# Output: true

# Example 2:

# Input: nums = [1, 2, 3, 4]
# Output: false

def contains_duplicate(nums):
    h = {}
    for i in range(len(nums)): # Looping through all value O(n) time 
        if nums[i] in h: # Single Check O(1) 
            return True
        h[nums[i]] = i # Single Insertion O(1)
    return False        

# Total Time = O(n) + O(1) + O(1) = O(n)
# Total Space = O(n)    

print(contains_duplicate([1,2,3,4,5,6,4]))  
# WE can do this the other way too usin set which is simpler

def contains_duplicate_Set(nums):
    s_nums = set(nums)
    if len(s_nums) != len(nums):
        return True 
    return False    

print(contains_duplicate_Set([1,2,3,4,5,6,4]))    


# for set time and space complexity is O(n)

