# https://leetcode.com/problems/jump-game-ii/
# leetcode 45 : Jump Game II
# LEVEL : Medium

class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)

        count = [10000] * len(nums)
        count[length-1] = 0

        jump = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > 0:
                count[i] = min(count[i+1:i+nums[i]+1]) + 1

        return count[0]
