# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# leetcode 34 : Find First and Last Position of Element in Sorted Array
# LEVEL : Medium

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binary_search(left, right, isFirst):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    if isFirst:
                        if mid == 0 or nums[mid-1] < target:
                            return mid
                        else:
                            right = mid - 1
                    else:
                        if mid == len(nums)-1 or nums[mid+1] > target:
                            return mid
                        else:
                            left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        return [binary_search(0, len(nums)-1, True), binary_search(0, len(nums)-1, False)]
