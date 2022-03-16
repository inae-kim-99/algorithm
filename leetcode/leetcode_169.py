# https://leetcode.com/problems/majority-element/
# leetcode 169 : Majority Element
# LEVEL : Easy

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        for num in set(nums):
            if nums.count(num) > n/2:
                return num
