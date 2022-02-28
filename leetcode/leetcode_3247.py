# https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3247/
# leetcode 3247 : deleting items from an array

class Solution:
    def removeElement(nums, val) -> int:
        while nums.count(val):
            nums.remove(val)
        return len(nums)
