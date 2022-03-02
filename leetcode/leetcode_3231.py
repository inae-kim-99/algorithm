# https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3231/
# leetcode : Third Maximum Number

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        if len(nums) < 3:
            return nums[-1]
        else:
            return nums[-3]
