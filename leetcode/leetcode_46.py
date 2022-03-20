# https://leetcode.com/problems/permutations/
# leetcode 46 : Permutations
# LEVEL : Medium

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(chosen, used):
            if len(chosen) == len(nums):
                result.append(chosen[:])
                return

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    chosen.append(nums[i])
                    dfs(chosen, used)
                    used[i] = False
                    chosen.pop()

        result = []
        used = [False for _ in range(len(nums))]

        dfs([], used)

        return result
