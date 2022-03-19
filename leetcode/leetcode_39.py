# https://leetcode.com/problems/combination-sum/
# leetcode 39 : Combination Sum
# LEVEL : Medium

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def findSum(remain, numbers, start):
            if remain == 0:
                answer.append(numbers)
                return
            elif remain < 0:
                return

            for i in range(start, len(candidates)):
                findSum(remain-candidates[i], numbers+[candidates[i]], i)

        findSum(target, [], 0)
        return answer


Solution.combinationSum(0, [2, 3, 6, 7], 7)
