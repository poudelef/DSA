# Top K Frequent Elements

# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.
# You may return the output in any order.

# Example 1:
# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]

# Example 2:
# Input: nums = [7,7], k = 1
# Output: [7]

def topKFrequent(nums: list, k: int) -> list:
    h = {}
    for i in range(len(nums)):
        h[nums[i]] = h.get(nums[i],0) + 1
    sort_h = sorted(h.items(), key= lambda x : x[1], reverse= True)
    v = []
    for k in sort_h[:k]:
        v.append(k[0]) 
    return v