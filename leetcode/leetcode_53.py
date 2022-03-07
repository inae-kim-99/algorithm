# https://leetcode.com/problems/maximum-subarray/
# leetcode 53 : Maximum Subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current, max_sum = 0, nums[0]
        for num in nums:
            current += num
            if current > max_sum:
                max_sum = current
            if current < 0:
                current = 0
        return max_sum
