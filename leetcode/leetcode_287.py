# https: // leetcode.com/problems/find-the-duplicate-number/
# leetcode 287 : Find the Duplicate Number
# LEVEL : Medium

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dict = {}
        for num in nums:
            if dict.get(num) == None:
                dict[num] = True
            else:
                return num
