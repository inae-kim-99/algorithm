# https://leetcode.com/problems/sort-colors/
# leetcode 75 : Sort Colors
# LEVEL : Medium

# Solution
# one-pass algorithm으로 풀이하라고 했으므로 요소를 하나씩 탐색하며 움직인다.
# white의 위치를 0부터 확인하는데,
# (1)
# 0(red)인 경우 white의 위치와 red의 위치를 바꾸고
# red index 를 1증가, white index를 1 증가시킨다.
# (2)
# 1(white)인 경우 white index를 1 증가시킨다.
# (3)
# 2(blue)인 경우 blue와 white 위치를 바꾸고, blue의 인덱스를 -1 감소시킨다.
# (blue는 마지막에 있어야 하기 때문에 맨 마지막 인덱스부터 채워 나간다.)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red = 0
        white = 0
        blue = len(nums)-1
        
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1