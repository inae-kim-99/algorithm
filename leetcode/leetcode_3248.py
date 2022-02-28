# https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3248/
# leetcode : Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        while idx < len(nums)-1:
            if nums[idx] == nums[idx+1]:
                nums.pop(idx)
            else:
                idx += 1

        return len(nums)
