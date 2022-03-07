# https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3228/
# leetcode : Height Checker

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        expected = sorted(heights)
        for e, h in zip(expected, heights):
            if e != h:
                count += 1
        return count
