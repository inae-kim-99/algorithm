# https://leetcode.com/problems/jump-game/
# leetcode 55 : Jump Game
# LEVEL : Medium

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = len(nums)-1
        
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= jump:
                jump = i
        
        return jump == 0