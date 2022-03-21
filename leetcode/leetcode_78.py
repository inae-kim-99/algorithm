# https://leetcode.com/problems/subsets/
# leetcode 78 : Subsets
# LEVEL : Medium
    
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def makeSubset(count, subset, index):
            if count == 0:
                result.append(subset[:])
                return
            elif index == len(nums):
                return
            
            makeSubset(count-1, subset+[nums[index]], index+1)
            makeSubset(count, subset, index+1)
        
        for i in range(len(nums)+1):
            makeSubset(i, [], 0)
        
        return result
                