# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# leetcode 153 : Find Minimum in Rotated Sorted Array
# LEVEL : Medium

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = (left + right) // 2
            
            if mid == len(nums)-1 or nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
                
        return nums[-1]
            