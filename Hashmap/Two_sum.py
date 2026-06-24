# Two Sum
# Easy
# Topics
# Company Tags
# Hints
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Example 1:

# Input: 
# nums = [3,4,5,6], target = 7

# Output: [0,1]

def two_sum(nums:list, target:int)->list:
    h = {}
    for i in range(len(nums)): # Time O(n)
        diff = target - nums[i]
        if diff in h: # O(1)
            return [h[diff], i]
        h[nums[i]] = i # O(1)

# Here worst case we have to loop through every element so time is O(n) and 
# space is O(n) as we might have to store every element before returning        

nums = [3,4,5,6]
target = 10

print(two_sum(nums,target))