# Two Integer Sum II

# Given an array of integers numbers that is sorted in non-decreasing order.
# Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. 
# Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

# There will always be exactly one valid solution.
# Your solution must use O(1) additional space.

# Example 1:
# Input: numbers = [1,2,3,4], target = 3
# Output: [1,2]

def two_sum(nums:list,target:int)->list:
    l = 0
    r = len(nums) -1
    while l < r:
        if nums[l] + nums[r] == target:
            return [l+1, r+1]
        elif nums[l] + nums[r] > target:
            r -=1 
        else:
            l+=1 

print(two_sum( nums= [1,2,3,4], target = 7))                    