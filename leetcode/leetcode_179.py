# https://leetcode.com/problems/largest-number/
# leetcode 179 : Largest Number
# LEVEL : Medium

# 풀이
# 어떤 숫자가 앞에 먼저 와야 최종 숫자가 클지 계산하는 문제이다.
# 숫자를 모두 string 으로 바꾼 후, "{num1}{num2}" "{num2}{num1}" 중에 뭐가 더 큰지 단순히 비교하면 된다.

from typing import List
from functools import cmp_to_key

class Solution:

    def compare(self, num1: str, num2: str) -> bool:
        if num1+num2 > num2+num1:
            return -1
        elif num1+num2 < num2+num1:
            return 1
        else:
            return 0

    def largestNumber(self, nums: List[int]) -> str:
        array = [str(num) for num in nums]
        array = sorted(array, key=cmp_to_key(self.compare))

        answer = ''.join(array).lstrip('0')
        
        return answer if answer else '0'




solution = Solution()
print(solution.largestNumber([10, 2]))
        
