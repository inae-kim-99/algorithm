# https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3157/
# leetcode : Move Zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count_zero = 0
        place = 0

        for num in nums:
            if num != 0:
                nums[place] = num
                place += 1
            else:
                count_zero += 1

        if count_zero > 0:
            nums[-count_zero:] = [0] * count_zero
