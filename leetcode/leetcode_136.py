# https://leetcode.com/problems/single-number/
# leetcode 136 : Single Number
# LEVEL : Easy

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        for i in range(0, len(nums)-1, 2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums.pop()
