# https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3270/
# leetcode 3270 : Find All Numbers Disappeared in an Array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        exists = [False for i in range(len(nums))]
        for num in range(nums):
            exists[num-1] = True
        answer = []
        for idx, is_exist in enumerate(exists):
            if not is_exist:
                answer.append(idx+1)
        return answer
