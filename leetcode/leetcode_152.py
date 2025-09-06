# https://leetcode.com/problems/maximum-product-subarray/description/
#
# 문제
# : 부분 연속 배열의 곱 중에 가장 큰 값을 구하기
# 풀이
# : 음수도 존재할 수 있기 때문에 현재의 최대값에 음수를 곱하면 다시 최소값이 된다.
#   각 원소를 보면서 현재의 최소값, 최대값을 저장하면서 최종 최대값을 업데이트한다.

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]

        max_result = nums[0]
        min_result = nums[0]

        for num in nums[1:]:

            candi1 = num
            candi2 = max_result * num
            candi3 = min_result * num

            max_result = max(candi1, candi2, candi3)
            min_result = min(candi1, candi2, candi3)

            result = max(result, max_result)

        return result



