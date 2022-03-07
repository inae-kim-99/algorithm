# https://leetcode.com/explore/learn/card/fun
# leetcode 3574 : Squares of a Sorted Array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [num*num for num in nums]
        nums.sort()
        return nums
