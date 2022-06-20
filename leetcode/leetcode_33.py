# https://leetcode.com/problems/search-in-rotated-sorted-array/
# leetcode 33 : Search in Rotated Sorted Array
# LEVEL : Medium

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find(left, right):
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid
               
                if nums[mid] < nums[right]: # right sorted array
                    if nums[mid] < target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
                else: # left sorted array
                    if nums[left] <= target < nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
            return -1
        
        
        return find(0, len(nums)-1)
                    