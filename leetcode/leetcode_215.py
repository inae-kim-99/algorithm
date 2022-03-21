# https://leetcode.com/problems/kth-largest-element-in-an-array/
# leetcode 215 : Kth Largest Element in an Array
# LEVEL : Medium

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[len(nums)-k]
