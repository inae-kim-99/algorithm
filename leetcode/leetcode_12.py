# https://leetcode.com/problems/3sum-closest/
# leetcode 16 : 3Sum Closet
# LEVEL : Medium

# 풀이
# 3개의 합을 비교하는 문제이므로 주어진 nums 배열을 정렬하고
# 원소 1개를 고정한 후, 나머지 2개의 원소를 가장 왼쪽, 오른쪽 원소에서 시작한다.
# 3개의 합이 target보다 작은 경우 왼쪽을 +1하고, target보다 큰 경우 오른쪽을 -1한다.


from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        length = len(nums)
        nums.sort()

        if length == 3:
            return sum(nums)

        min_diff = sum(nums[:3]) - target

        for p1 in range(length - 2):

            p2, p3 = p1 + 1, length - 1
            while p2 < p3:
                cur_sum = nums[p1] + nums[p2] + nums[p3]
                            
                if cur_sum < target:
                    p2 += 1
                elif cur_sum > target:
                    p3 -= 1
                else:
                    return target
                
                if abs(cur_sum - target) < abs(min_diff):
                    min_diff = cur_sum - target

        return target + min_diff


solution = Solution()
print(solution.threeSumClosest([1,1,1,1], 0))

