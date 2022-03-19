# https://leetcode.com/problems/container-with-most-water/
# leetcode 11 : Container With Most Water
# LEVEL : Medium

# two pointer를 통해 해결.
# 첫번째와 마지막 height의 container를 계산하고
# 둘 중 height가 더 작은 곳을 움직여가며
# max_congtainer를 계산한다.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height)-1
        max_container = 0
        while start != end:
            container = (end-start)*min(height[start], height[end])
            max_container = max(container, max_container)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_container
