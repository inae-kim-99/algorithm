# https://leetcode.com/problems/search-insert-position/
# leetcode 35 : Search Insert Position
# LEVEL : Easy

class Solution:
    def searchInsert(nums, target) -> int:
        start, end = 0, len(nums)
        while start < end:
            index = (start + end) // 2
            if nums[index] == target:
                return index
            elif nums[index] < target:
                start = index + 1
            else:
                end = index
        return end


nums = [1,3,5,6]
target = 2
Solution.searchInsert(nums, target)
                