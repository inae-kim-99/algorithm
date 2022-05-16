# https://leetcode.com/problems/3sum/
# leetcode 15 : 3Sum
# LEVEL : Medium

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        
        for i in range(0, len(nums)-2):
            left, right = i+1, len(nums)-1
            
            while left < right:
                s = nums[i] + nums[left] + nums[right] 
                if s == 0:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif s > 0:
                    right -= 1
                else:
                    left += 1
                    
        return list(res)